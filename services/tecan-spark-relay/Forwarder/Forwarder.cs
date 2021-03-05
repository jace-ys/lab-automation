using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using System.Net.Http;

using Newtonsoft.Json;

namespace TecanSparkRelay.Forwarder
{
  public class Forwarder
  {
    private readonly HttpClient client = new HttpClient();
    private readonly string dataGatewayAddr;

    public Forwarder(ForwarderConfig cfg)
    {
      this.dataGatewayAddr = cfg.DataGatewayAddr;
    }

    public async Task Forward(string uuid, Data data)
    {
      var payload = JsonConvert.SerializeObject(new Dictionary<string, dynamic>{
        {"uuid", uuid},
        {"data", data}
      });
      Console.WriteLine(payload);

      var content = new StringContent(payload, Encoding.UTF8, "application/json");
      var response = await this.client.PostAsync($"http://{this.dataGatewayAddr}/data", content);
      var responseString = await response.Content.ReadAsStringAsync();
      Console.WriteLine(responseString);
    }
  }
}
