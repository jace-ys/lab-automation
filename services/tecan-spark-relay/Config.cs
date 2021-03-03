using System;
using System.Collections;

namespace TecanSparkRelay
{
  public class Config
  {
    public ManagerConfig manager;
    public RedisPubSubConfig pubsub;

    public Config()
    {
      IDictionary config = Environment.GetEnvironmentVariables();

      this.manager = new ManagerConfig(config);
      this.pubsub = new RedisPubSubConfig(config);
    }
  }

  public class ManagerConfig
  {
    public int INSTRUMENT = 1910012500;

    public ManagerConfig(IDictionary config)
    {
      int instrument;
      if (Int32.TryParse(config["MANAGER_INSTRUMENT"]?.ToString(), out instrument))
      {
        this.INSTRUMENT = instrument;
      }
    }
  }

  public class RedisPubSubConfig
  {
    public string ADDR = "127.0.0.1:6389";
    public string SUBSCRIPTION_TOPIC = "TecanSpark/v1alpha1";

    public RedisPubSubConfig(IDictionary config)
    {
      this.ADDR = config["REDIS_PUBSUB_ADDR"]?.ToString() ?? this.ADDR;
      this.SUBSCRIPTION_TOPIC = config["REDIS_PUBSUB_SUBSCRIPTION_TOPIC"]?.ToString() ?? this.SUBSCRIPTION_TOPIC;
    }
  }
}
