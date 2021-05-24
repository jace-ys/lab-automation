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
        private readonly string dataGatewayURL;

        public Forwarder(ForwarderConfig cfg)
        {
            this.dataGatewayURL = cfg.DataGatewayURL;
        }

        public async Task Forward(string uuid, DataRow row)
        {
            // Serialize the data to JSON
            var payload = JsonConvert.SerializeObject(new Dictionary<string, dynamic>{
                {"uuid", uuid},
                {"row", row}
            });

            try
            {
                // Forward the data to the service.data-gateway
                var content = new StringContent(payload, Encoding.UTF8, "application/json");
                var response = await this.client.PostAsync($"{this.dataGatewayURL}/data", content);
            }
            catch (HttpRequestException ex)
            {
                throw new ApplicationException(ex.Message);
            }
        }

        public async Task BatchForward(string uuid, List<DataRow> rows)
        {
            // Serialize the data to JSON
            var payload = JsonConvert.SerializeObject(new Dictionary<string, dynamic>{
                {"uuid", uuid},
                {"rows", rows}
            });

            try
            {
                // Forward the data to the service.data-gateway
                var content = new StringContent(payload, Encoding.UTF8, "application/json");
                var response = await this.client.PostAsync($"{this.dataGatewayURL}/data/batch", content);
            }
            catch (HttpRequestException ex)
            {
                throw new ApplicationException(ex.Message);
            }
        }

        public List<DataRow> ParseResults(string resultsXML, Protocols.Plate plate)
        {
            XmlSerializer serializer = new XmlSerializer(typeof(System.MeasurementResultData));
            using (TextReader reader = new StringReader(resultsXML))
            {
                // Parse the XML measurement data
                System.MeasurementResultData data = (System.MeasurementResultData)serializer.Deserialize(reader);

                // Convert the measurement data to data rows that the service.data-gateway is able to accept
                List<DataRow> rows = data.Absorbance.DataLabel.ResultContext.Select(result =>
                {
                    return new DataRow(result, plate);
                }).ToList();

                return rows;
            }
        }
    }
}
