using System;
using System.Collections;

namespace TecanSparkRelay
{
  public class Config
  {

    public string pubsubAddr = "127.0.0.1:6389";
    public string pubsubSubscriptionTopic = "TecanSpark/v1alpha1";

    public Config()
    {
      IDictionary config = Environment.GetEnvironmentVariables();

      this.pubsubAddr = config["REDIS_PUBSUB_ADDR"]?.ToString() ?? this.pubsubAddr;
      this.pubsubSubscriptionTopic = config["REDIS_PUBSUB_SUBSCRIPTION_TOPIC"]?.ToString() ?? this.pubsubSubscriptionTopic;
    }
  }
}
