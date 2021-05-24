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

        public DataRow(System.ResultContext result, Protocols.Plate plate)
        {
            var measurement = result.MeasurementResult;
            this.data = new Data(measurement.TimeStamp, measurement.Value);

            // Translate row-first to column-first well indexing as per the conventions
            // for plate-based protocols
            var well = Int16.Parse(result.WellIndex);
            this.index = (well / plate.columns) + ((well % plate.columns) * plate.rows);
        }
    }

    public class Data
    {
        public string timeElapsed;
        public string absorbance;
        public string error;

        public Data(string timeElapsed, string absorbance)
        {
            this.timeElapsed = timeElapsed;
            this.absorbance = absorbance;
        }

        public Data(Exception ex)
        {
            this.error = ex.Message;
        }
    }
}
