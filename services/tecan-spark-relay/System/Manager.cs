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
                this.logger.Information("trigger.received, {trigger}", message);

                Trigger trigger = new Trigger();
                try
                {
                    trigger = JsonConvert.DeserializeObject<Trigger>(message);

                    if (this.running)
                    {
                        throw new ApplicationException("An existing experiment is already running");
                    }

                    this.HandleTrigger(trigger);
                }
                catch (ApplicationException ex)
                {
                    this.logger.Error("[experiment.create.failed] {uuid} {error}", trigger.uuid, ex.Message);
                    this.ForwardError(trigger, ex);
                }
                catch (Exception ex)
                {
                    this.logger.Error("[experiment.create.failed] {uuid} {error}", trigger.uuid, ex.Message);
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

        void HandleTrigger(Trigger trigger)
        {
            string methodXML = "";
            try
            {
                trigger.spec.Validate();
                methodXML = trigger.spec.GenerateMethodXML();

                IEnumerable<string> messages;
                if (!this.ai.CheckMethod(this.instrument, methodXML, trigger.protocol, out messages))
                {
                    string msg = string.Join(", ", messages);
                    throw new ApplicationException(msg);
                }
            }
            catch (Exception ex)
            {
                throw new ApplicationException($"Error generating method XML for {trigger.protocol}: {ex.Message}");
            }

            new Task(async () =>
                {
                    this.running = true;

                    MethodExecutionResult result = null;
                    try
                    {
                        this.logger.Information("[experiment.execute.started] {uuid}", trigger.uuid);
                        result = this.ai.ExecuteMethod(this.instrument, methodXML, trigger.protocol, false);
                        this.logger.Information("[experiment.execute.finished] {uuid} {workspace} {execution}", trigger.uuid, result.WorkspaceId, result.ExecutionId);
                    }
                    catch (Exception ex)
                    {
                        this.logger.Error("[experiment.execute.failed] {uuid} {error}", trigger.uuid, ex.Message);
                        this.ForwardError(trigger, ex);
                        return;
                    }
                    finally
                    {
                        this.running = false;
                    }

                    try
                    {
                        var resultsXML = File.ReadAllText(this.ai.GetResults(result.WorkspaceId, result.ExecutionId));
                        var rows = this.forwarder.ParseResults(resultsXML, trigger.spec.Plate()).Where(row => row.index < trigger.spec.wells.Count).ToList();

                        this.logger.Information("[batch.forward.started] {uuid} {rows}", trigger.uuid, rows.Count);
                        await this.forwarder.BatchForward(trigger.uuid, rows);
                        this.logger.Information("[batch.forward.finished] {uuid} {rows}", trigger.uuid, rows.Count);
                    }
                    catch (Exception ex)
                    {
                        this.logger.Error("[batch.forward.failed] {uuid} {error}", trigger.uuid, ex.Message);
                    }
                }).Start();
        }

        async void ForwardError(Trigger trigger, Exception err)
        {
            try
            {
                var data = new Forwarder.Data(err);
                var row = new Forwarder.DataRow(data);
                await this.forwarder.Forward(trigger.uuid, row);
                this.logger.Information("[configure.error.forwarded {uuid}", trigger.uuid);
            }
            catch (ApplicationException ex)
            {
                this.logger.Error("[configure.error.forward.failed {uuid} {error}", trigger.uuid, ex.Message);
            }
        }
    }
}
