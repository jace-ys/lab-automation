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
        public Methods.SparkMethod spec { get; set; }
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

            var trigger = new Trigger();
            var methodName = (string)obj["protocol"];
            var method = Methods.Registry.GetMethod(methodName);

            foreach (var well in obj["spec"])
            {
                var spec = Activator.CreateInstance(method.SpecType());
                serializer.Populate(well.CreateReader(), spec);
                method.wells.Add(spec);
            }
            obj.Remove("spec");

            trigger.spec = method;
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
