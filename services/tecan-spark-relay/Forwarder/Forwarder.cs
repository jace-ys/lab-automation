using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Serialization;

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

        public async Task Forward(string uuid, DataRow row)
        {
            var payload = JsonConvert.SerializeObject(new Dictionary<string, dynamic>{
                {"uuid", uuid},
                {"row", row}
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

        public async Task BatchForward(string uuid, List<DataRow> rows)
        {
            var payload = JsonConvert.SerializeObject(new Dictionary<string, dynamic>{
                {"uuid", uuid},
                {"rows", rows}
            });

            try
            {
                var content = new StringContent(payload, Encoding.UTF8, "application/json");
                var response = await this.client.PostAsync($"http://{this.dataGatewayAddr}/data/batch", content);
            }
            catch (HttpRequestException ex)
            {
                throw new ApplicationException(ex.Message);
            }
        }

        public List<DataRow> ParseResults(string resultsXML, Methods.Plate plate)
        {
            XmlSerializer serializer = new XmlSerializer(typeof(System.MeasurementResultData));
            using (TextReader reader = new StringReader(resultsXML))
            {
                System.MeasurementResultData data = (System.MeasurementResultData)serializer.Deserialize(reader);

                List<DataRow> rows = data.Absorbance.DataLabel.ResultContext.Select(result =>
                {
                    return new DataRow(result, plate);
                }).ToList();

                return rows;
            }
        }
    }
}
