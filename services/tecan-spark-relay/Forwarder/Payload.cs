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

        public DataRow(System.ResultContext result, Methods.Plate plate)
        {
            var measurement = result.MeasurementResult;
            this.data = new Data(measurement.TimeStamp, measurement.Value);

            // Translate row-first to column-first well indexing as per protocol conventions
            var well = Int16.Parse(result.WellIndex);
            this.index = (well / plate.columns) + ((well % plate.columns) * plate.rows);
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
