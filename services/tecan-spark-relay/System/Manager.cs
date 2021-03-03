using System;
using System.IO;
using System.Linq;
using System.Threading.Tasks;

using Serilog;
using ServiceStack.Redis;
using Newtonsoft.Json;

namespace TecanSparkRelay.System
{
  public class Manager
  {
    private ILogger logger;
    private IRedisSubscription subscription;
    private AutomationInterface ai;

    private int instrument;
    private string topic;
    private bool running = false;
    private Object mutex = new Object();

    public Manager(ILogger logger, AutomationInterface ai, RedisClient redis, string topic, ManagerConfig cfg)
    {
      this.logger = logger;
      this.subscription = redis.CreateSubscription();
      this.ai = ai;
      this.topic = topic;

      this.SetInstrument(cfg.INSTRUMENT);

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

        try
        {
          lock (mutex)
          {
            if (this.running)
            {
              throw new ApplicationException("An existing experiment is already running");
            }
          }

          this.HandleCommand(message);
        }
        catch (Exception ex)
        {
          this.logger.Error("[experiment.create.failed] {error}", ex.Message);
        }
      };

      this.subscription.SubscribeToChannels(new string[] { this.topic
  });
      return;
    }

    public void Unsubscribe()
    {
      this.subscription.UnSubscribeFromAllChannels();
    }

    void SetInstrument(int selectedInstrument)
    {
      this.instrument = this.ai.GetInstruments().FirstOrDefault(i => i == selectedInstrument);
      if (this.instrument == 0)
      {
        throw new ApplicationException($"Could not find an instrument with serial {selectedInstrument}");
      }
    }

    void HandleCommand(string message)
    {
      var command = JsonConvert.DeserializeObject<Command>(message);

      string methodXML;
      try
      {
        command.spec.Validate();
        methodXML = command.spec.GenerateMethodXML();
        Console.WriteLine(methodXML);
      }
      catch (Exception ex)
      {
        throw new ApplicationException($"Error generating method XML for {command.protocol}: {ex.Message}");
      }

      new Task(() =>
        {
          try
          {
            lock (mutex)
            {
              this.running = true;
            }
            var (workspaceId, executionId) = this.ai.ExecuteMethod(this.instrument, methodXML, command.protocol, false);
            lock (mutex)
            {
              this.running = false;
            }

            var resultsXML = File.ReadAllText(this.ai.GetResults(workspaceId, executionId));
            Console.WriteLine($"Results:\n{resultsXML}");
          }
          catch (Exception ex)
          {
            this.logger.Error("[experiment.execute.failed] {error}", ex.Message);
          }
        }).Start();
    }
  }
}
