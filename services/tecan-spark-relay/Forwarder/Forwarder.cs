using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
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

            try
            {
                var content = new StringContent(payload, Encoding.UTF8, "application/json");
                var response = await this.client.PostAsync($"http://{this.dataGatewayAddr}/data", content);
            }
            catch (HttpRequestException ex)
            {
                throw new ApplicationException(ex.Message);
            }
        }
    }
}
