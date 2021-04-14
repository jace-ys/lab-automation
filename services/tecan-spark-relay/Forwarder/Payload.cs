using System;

namespace TecanSparkRelay.Forwarder
{
    public class DataRow
    {
        public Data data;
        public int? index;

        public DataRow(Data data)
        {
            this.data = data;
        }

        public DataRow(System.ResultContext result)
        {
            var measurement = result.MeasurementResult;
            this.data = new Data(measurement.TimeStamp, measurement.Value);
            this.index = Int16.Parse(result.WellIndex);
        }
    }

    public class Data
    {
        public string expTime;
        public string odMeasured;
        public string error;

        public Data(string expTime, string odMeasured)
        {
            this.expTime = expTime;
            this.odMeasured = odMeasured;
        }

        public Data(Exception ex)
        {
            this.error = ex.Message;
        }
    }
}
