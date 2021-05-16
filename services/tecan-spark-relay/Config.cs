using System;
using System.Collections;

namespace TecanSparkRelay
{
    public class Config
    {
        public string version = "TecanSpark/v1alpha1";
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
        public string DataGatewayURL;

        public ForwarderConfig(IDictionary config)
        {
            this.DataGatewayURL = config["FORWARDER_DATA_GATEWAY_URL"].ToString() ?? this.DataGatewayURL;
        }
    }

    public class ManagerConfig
    {
        public string DeviceName = "";
        public string Instrument = "1910012500";

        public ManagerConfig(IDictionary config)
        {
            this.DeviceName = config["MANAGER_DEVICE_NAME"]?.ToString() ?? this.DeviceName;
            this.Instrument = config["MANAGER_INSTRUMENT"]?.ToString() ?? this.Instrument;
        }
    }

    public class RedisPubSubConfig
    {
        public string URL = "redis://127.0.0.1:6389";

        public RedisPubSubConfig(IDictionary config)
        {
            this.URL = config["REDIS_PUBSUB_URL"]?.ToString() ?? this.URL;
        }
    }
}
