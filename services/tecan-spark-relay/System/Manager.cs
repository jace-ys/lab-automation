using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading.Tasks;

using Newtonsoft.Json;
using Serilog;
using ServiceStack.Redis;
using Tecan.At.Dragonfly.AutomationInterface.Data;

namespace TecanSparkRelay.System
{
    public class Manager
    {
        private readonly ILogger logger;
        private readonly Forwarder.Forwarder forwarder;
        private readonly IRedisSubscription subscription;
        private readonly string topic;
        private readonly AutomationInterface ai = new FakeAutomationInterface();

        private Instrument instrument;
        private bool running = false;

        public Manager(ILogger logger, Forwarder.Forwarder forwarder, RedisClient redis, string topic, ManagerConfig cfg)
        {
            this.logger = logger;
            this.forwarder = forwarder;
            this.subscription = redis.CreateSubscription();
            this.topic = topic;
            this.SetInstrument(cfg.Instrument);

            JsonConvert.DefaultSettings = () => new JsonSerializerSettings
            {
                MissingMemberHandling = MissingMemberHandling.Error,
            };
        }

        public static void Init() { }

        public static string ExportMethod(string methodName)
        {

            return new FakeAutomationInterface().GetMethodXml(methodName);
        }

        public void Subscribe()
        {
            subscription.OnMessage = (topic, message) =>
            {
                this.logger.Information("command.received, {command}", message);

                Command command = new Command();
                try
                {
                    command = JsonConvert.DeserializeObject<Command>(message);

                    if (this.running)
                    {
                        throw new ApplicationException("An existing experiment is already running");
                    }

                    this.HandleCommand(command);
                }
                catch (ApplicationException ex)
                {
                    this.logger.Error("[experiment.create.failed] {uuid} {error}", command.uuid, ex.Message);
                    this.ForwardError(command, ex);
                }
                catch (Exception ex)
                {
                    this.logger.Error("[experiment.create.failed] {uuid} {error}", command.uuid, ex.Message);
                }
            };

            this.subscription.SubscribeToChannels(new string[] { this.topic });
        }

        public void Shutdown()
        {
            this.subscription.UnSubscribeFromAllChannels();
        }

        void SetInstrument(string selectedInstrument)
        {
            this.instrument = this.ai.GetInstruments().FirstOrDefault(i => i.SerialNumber == selectedInstrument);
            if (this.instrument is null)
            {
                throw new ApplicationException($"Could not find an instrument with serial {selectedInstrument}");
            }

            if (this.instrument.State != InstrumentState.FullyOperational)
            {
                throw new ApplicationException($"Instrument with serial {selectedInstrument} is not fully operational");
            }
        }

        void HandleCommand(Command command)
        {
            string methodXML = "";
            try
            {
                command.spec.Validate();
                methodXML = command.spec.GenerateMethodXML();

                IEnumerable<string> messages;
                if (!this.ai.CheckMethod(this.instrument, methodXML, command.protocol, out messages))
                {
                    string msg = string.Join(", ", messages);
                    throw new ApplicationException(msg);
                }
            }
            catch (Exception ex)
            {
                throw new ApplicationException($"Error generating method XML for {command.protocol}: {ex.Message}");
            }

            new Task(async () =>
                {
                    this.running = true;

                    MethodExecutionResult result = null;
                    try
                    {
                        this.logger.Information("[experiment.execute.started] {uuid}", command.uuid);
                        result = this.ai.ExecuteMethod(this.instrument, methodXML, command.protocol, false);
                        this.logger.Information("[experiment.execute.finished] {uuid} {workspace} {execution}", command.uuid, result.WorkspaceId, result.ExecutionId);
                    }
                    catch (Exception ex)
                    {
                        this.logger.Error("[experiment.execute.failed] {uuid} {error}", command.uuid, ex.Message);
                        this.ForwardError(command, ex);
                        return;
                    }
                    finally
                    {
                        this.running = false;
                    }

                    try
                    {
                        var resultsXML = File.ReadAllText(this.ai.GetResults(result.WorkspaceId, result.ExecutionId));
                        var rows = this.forwarder.ParseResults(resultsXML, command.spec.Plate()).Where(row => row.index < command.spec.wells.Count).ToList();

                        this.logger.Information("[batch.forward.started] {uuid} {rows}", command.uuid, rows.Count);
                        await this.forwarder.BatchForward(command.uuid, rows);
                        this.logger.Information("[batch.forward.finished] {uuid} {rows}", command.uuid, rows.Count);
                    }
                    catch (Exception ex)
                    {
                        this.logger.Error("[batch.forward.failed] {uuid} {error}", command.uuid, ex.Message);
                    }
                }).Start();
        }

        async void ForwardError(Command command, Exception err)
        {
            try
            {
                var data = new Forwarder.Data(err);
                var row = new Forwarder.DataRow(data);
                await this.forwarder.Forward(command.uuid, row);
                this.logger.Information("[configure.error.forwarded {uuid}", command.uuid);
            }
            catch (ApplicationException ex)
            {
                this.logger.Error("[configure.error.forward.failed {uuid} {error}", command.uuid, ex.Message);
            }
        }
    }
}
