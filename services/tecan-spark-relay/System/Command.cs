using System;
using System.Collections.Generic;

using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

namespace TecanSparkRelay.System
{
  [JsonConverter(typeof(CommandConverter))]
  class Command
  {
    public string uuid { get; set; }
    public string apiVersion { get; set; }
    public string protocol { get; set; }
    public Methods.SparkMethod spec { get; set; }
    public CommandMetadata metadata { get; set; }
  }

  public class CommandConverter : JsonConverter
  {
    public override bool CanConvert(Type objectType)
    {
      return (objectType == typeof(Command));
    }

    public override object ReadJson(JsonReader reader, Type objectType, object existingValue, JsonSerializer serializer)
    {
      JObject obj = JObject.Load(reader);

      var command = new Command();
      var methodName = (string)obj["protocol"];
      command.spec = Methods.Registry.GetMethod(methodName);
      serializer.Populate(obj.CreateReader(), command);

      return command;
    }

    public override void WriteJson(JsonWriter writer, object value, JsonSerializer serializer)
    {
      throw new NotImplementedException();
    }
  }

  class CommandMetadata
  {
    public CommandSource source { get; set; }
  }

  class CommandSource
  {
    public string name { get; set; }
    public Dictionary<string, dynamic> spec { get; set; }
  }
}
