using System;
using System.Collections;

namespace TecanSparkRelay
{
    public class Config
    {
        public readonly ForwarderConfig forwarder;
        public readonly ManagerConfig manager;
        public readonly RedisPubSubConfig pubsub;

        public Config()
        {
            IDictionary config = Environment.GetEnvironmentVariables();

            this.forwarder = new ForwarderConfig(config);
            this.manager = new ManagerConfig(config);
            this.pubsub = new RedisPubSubConfig(config);
        }
    }

    public class ForwarderConfig
    {
        public string DataGatewayAddr;

        public ForwarderConfig(IDictionary config)
        {
            this.DataGatewayAddr = config["FORWARDER_DATA_GATEWAY_ADDR"].ToString() ?? this.DataGatewayAddr;
        }
    }

    public class ManagerConfig
    {
        public string Instrument = "1910012500";

        public ManagerConfig(IDictionary config)
        {
            this.Instrument = config["MANAGER_INSTRUMENT"]?.ToString() ?? this.Instrument;
        }
    }

    public class RedisPubSubConfig
    {
        public string Addr = "127.0.0.1:6389";
        public string SubscriptionTopic = "TecanSpark/v1alpha1";

        public RedisPubSubConfig(IDictionary config)
        {
            this.Addr = config["REDIS_PUBSUB_ADDR"]?.ToString() ?? this.Addr;
            this.SubscriptionTopic = config["REDIS_PUBSUB_SUBSCRIPTION_TOPIC"]?.ToString() ?? this.SubscriptionTopic;
        }
    }
}
