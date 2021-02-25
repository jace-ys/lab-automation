using System;

using Serilog;
using ServiceStack.Redis;

namespace TecanSparkRelay
{
  public class Manager
  {
    private ILogger logger;
    private IRedisSubscription subscription;
    private string topic;

    public Manager(ILogger logger, RedisClient redis, string topic)
    {
      this.logger = logger;
      this.subscription = redis.CreateSubscription();
      this.topic = topic;
    }

    public void Subscribe()
    {
      subscription.OnMessage = (channel, msg) =>
      {
        this.logger.Information(msg);
        throw new NotImplementedException();
      };

      this.subscription.SubscribeToChannels(new string[] { this.topic });
      return;
    }

    public void Unsubscribe()
    {
      this.subscription.UnSubscribeFromAllChannels();
    }
  }
}
