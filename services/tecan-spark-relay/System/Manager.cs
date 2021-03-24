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

        private readonly Object mutex = new Object();
        private readonly string topic;
        private IInstrument instrument;
        private bool running = false;

        public Manager(ILogger logger, Forwarder.Forwarder forwarder, RedisClient redis, string topic, ManagerConfig cfg)
        {
            this.logger = logger;
            this.forwarder = forwarder;
            this.subscription = redis.CreateSubscription();
            this.topic = topic;

            AutomationInterfaceFactory.Start();
            this.SetInstrument(cfg.Instrument);

            JsonConvert.DefaultSettings = () => new JsonSerializerSettings
            {
                MissingMemberHandling = MissingMemberHandling.Error,
            };
        }

        public void Subscribe()
        {
            subscription.OnMessage = (channel, message) =>
            {
                this.logger.Information("command.received, {command}", message);

                Command command = new Command();
                try
                {
                    command = JsonConvert.DeserializeObject<Command>(message);

                    lock (mutex)
                    {
                        if (this.running)
                        {
                            throw new ApplicationException("An existing experiment is already running");
                        }
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

        public void Unsubscribe()
        {
            this.subscription.UnSubscribeFromAllChannels();
        }

        void SetInstrument(string selectedInstrument)
        {
            using (var ai = AutomationInterfaceFactory.Build())
            {
                this.instrument = ai.InstrumentManagement.GetInstruments().FirstOrDefault(i => i.SerialNumber == selectedInstrument);
                if (this.instrument == null)
                {
                    throw new ApplicationException($"Could not find an instrument with serial {selectedInstrument}");
                }
            }

            if (this.instrument.State != InstrumentState.FullyOperational)
            {
                throw new ApplicationException($"Instrument with serial {selectedInstrument} is not fully operational");
            }
        }

        void HandleCommand(Command command)
        {
            string methodXML;
            try
            {
                command.spec.Validate();
                methodXML = command.spec.GenerateMethodXML();

                IEnumerable<string> messages;
                using (var ai = AutomationInterfaceFactory.Build())
                {
                    if (!ai.MethodExecution.CheckMethod(this.instrument, methodXML, command.protocol, out messages))
                    {
                        string msg = string.Join(", ", messages);
                        throw new ApplicationException(msg);
                    }
                }
            }
            catch (Exception ex)
            {
                throw new ApplicationException($"Error generating method XML for {command.protocol}: {ex.Message}");
            }

            new Task(() =>
              {
                  try
                  {
                      using (var ai = AutomationInterfaceFactory.Build())
                      {
                          this.logger.Information("[experiment.execute.started] {uuid}", command.uuid);
                          lock (mutex)
                          {
                              this.running = true;
                          }
                          var result = ai.MethodExecution.ExecuteMethod(this.instrument, methodXML, command.protocol, false);
                          lock (mutex)
                          {
                              this.running = false;
                          }
                          this.logger.Information("[experiment.execute.finished] {uuid} {workspace} {exeution}", command.uuid, result.WorkspaceId, result.ExecutionId);

                          var resultsXML = File.ReadAllText(ai.MethodExecution.GetResults(result.WorkspaceId, result.ExecutionId));
                          Console.WriteLine($"Results:\n{resultsXML}");
                      }
                  }
                  catch (Exception ex)
                  {
                      this.logger.Error("[experiment.execute.failed] {uuid} {error}", command.uuid, ex.Message);
                      this.ForwardError(command, ex);
                  }
                  finally
                  {
                      lock (mutex)
                      {
                          this.running = false;
                      }
                  }
              }).Start();
        }

        async void ForwardError(Command command, Exception err)
        {
            try
            {
                var data = new Forwarder.Data();
                data.Error(err);
                await this.forwarder.Forward(command.uuid, data);
                this.logger.Information("[configure.error.forwarded {uuid}", command.uuid);
            }
            catch (ApplicationException ex)
            {
                this.logger.Error("[configure.error.forward.failed {uuid} {error}", command.uuid, ex.Message);
            }
        }
    }
}
