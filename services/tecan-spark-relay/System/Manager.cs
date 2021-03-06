using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading.Tasks;

using Newtonsoft.Json;
using Serilog;
using ServiceStack.Redis;
using Tecan.At.Dragonfly.AutomationInterface;
using Tecan.At.Dragonfly.AutomationInterface.Data;

namespace TecanSparkRelay.System
{
    public class Manager
    {
        private readonly ILogger logger;
        private readonly Forwarder.Forwarder forwarder;
        private readonly IRedisSubscription subscription;
        private readonly string topic;

        private IInstrument instrument;
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

        public static void Init()
        {
            AutomationInterfaceFactory.Start();
        }

        public static string ExportMethod(string methodName)
        {
            using (var ai = AutomationInterfaceFactory.Build())
            {
                return ai.Queries.GetMethodXml(methodName);
            }
        }

        public void Subscribe()
        {
            subscription.OnMessage = (topic, message) =>
            {
                this.logger.Information("trigger.received, {trigger}", message);

                Trigger trigger = new Trigger();
                try
                {
                    // Deserialize the incoming protocol trigger
                    trigger = JsonConvert.DeserializeObject<Trigger>(message);

                    // Return an error if we are currently running a method
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
            AutomationInterfaceFactory.Stop();
        }

        void SetInstrument(string selectedInstrument)
        {
            using (var ai = AutomationInterfaceFactory.Build())
            {
                // Set the instrument to the selected one
                this.instrument = ai.InstrumentManagement.GetInstruments().FirstOrDefault(i => i.SerialNumber == selectedInstrument);
                if (this.instrument is null)
                {
                    throw new ApplicationException($"Could not find an instrument with serial {selectedInstrument}");
                }
            }

            // Check that the instrument is operational
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
                // Validate the protocol spec and generate a method XML
                trigger.spec.Validate();
                methodXML = trigger.spec.GenerateMethodXML();

                // Check that the method XML file is valid
                IEnumerable<string> messages;
                using (var ai = AutomationInterfaceFactory.Build())
                {
                    if (!ai.MethodExecution.CheckMethod(this.instrument, methodXML, trigger.protocol, out messages))
                    {
                        string msg = string.Join(", ", messages);
                        throw new ApplicationException(msg);
                    }
                }
            }
            catch (Exception ex)
            {
                throw new ApplicationException($"Error generating method XML for {trigger.protocol}: {ex.Message}");
            }

            new Task(async () =>
                {
                    this.running = true;

                    // Execute the method XML file
                    IMethodExecutionResult result = null;
                    try
                    {
                        using (var ai = AutomationInterfaceFactory.Build())
                        {
                            this.logger.Information("[experiment.execute.started] {uuid}", trigger.uuid);
                            result = ai.MethodExecution.ExecuteMethod(this.instrument, methodXML, trigger.protocol, false);
                            this.logger.Information("[experiment.execute.finished] {uuid} {workspace} {execution}", trigger.uuid, result.WorkspaceId, result.ExecutionId);
                        }
                    }
                    catch (Exception ex)
                    {
                        this.logger.Error("[experiment.execute.failed] {uuid} {error}", trigger.uuid, ex.Message);
                        this.ForwardError(trigger, ex);
                    }
                    finally
                    {
                        this.running = false;
                    }

                    try
                    {
                        using (var ai = AutomationInterfaceFactory.Build())
                        {
                            // Read and parse the file containing the XML measurement data
                            var resultsXML = File.ReadAllText(ai.MethodExecution.GetResults(result.WorkspaceId, result.ExecutionId));
                            var rows = this.forwarder.ParseResults(resultsXML, trigger.spec.Plate()).Where(row => row.index < trigger.spec.wells.Count).ToList();

                            this.logger.Information("[batch.forward.started] {uuid} {rows}", trigger.uuid, rows.Count);
                            // Forward the data to the service.data-gateway
                            await this.forwarder.BatchForward(trigger.uuid, rows);
                            this.logger.Information("[batch.forward.finished] {uuid} {rows}", trigger.uuid, rows.Count);
                        }
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
