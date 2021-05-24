using System;
using System.Collections.Generic;

using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

namespace TecanSparkRelay.System
{
    [JsonConverter(typeof(TriggerConverter))]
    class Trigger
    {
        public string uuid { get; set; }
        public string apiVersion { get; set; }
        public string protocol { get; set; }
        public Plate plate { get; set; }
        public Protocols.Protocol spec { get; set; }
        public TriggerMetadata metadata { get; set; }
    }

    public class TriggerConverter : JsonConverter
    {
        public override bool CanConvert(Type objectType)
        {
            return (objectType == typeof(Trigger));
        }

        public override object ReadJson(JsonReader reader, Type objectType, object existingValue, JsonSerializer serializer)
        {
            JObject obj = JObject.Load(reader);

            // Get the corresponding based on the trigger's protocol name
            var trigger = new Trigger();
            var protocolName = (string)obj["protocol"];
            var protocol = Protocols.Registry.GetProtocol(protocolName);

            // Loop through the wells in the protocol's spec
            foreach (var well in obj["spec"])
            {
                // Deserialize each spec object and add it to the list of wells
                var spec = Activator.CreateInstance(protocol.SpecType());
                serializer.Populate(well.CreateReader(), spec);
                protocol.wells.Add(spec);
            }
            obj.Remove("spec");

            // Set the protocol's spec object
            trigger.spec = protocol;
            serializer.Populate(obj.CreateReader(), trigger);

            return trigger;
        }

        public override void WriteJson(JsonWriter writer, object value, JsonSerializer serializer)
        {
            throw new NotImplementedException();
        }
    }

    class Plate
    {
        public int rows { get; set; }
        public int columns { get; set; }
    }

    class TriggerMetadata
    {
        public string source { get; set; }
        public List<Dictionary<string, dynamic>> spec { get; set; }
    }
}
