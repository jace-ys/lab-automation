using System;

namespace TecanSparkRelay.Forwarder
{
    public class DataRow
    {
        public string expTime;
        public string odMeasured;
        public string error = "";

        public DataRow() { }

        public DataRow(string expTime, string odMeasured)
        {
            this.expTime = expTime;
            this.odMeasured = odMeasured;
        }

        public void Error(Exception ex)
        {
            this.error = ex.Message;
        }
    }
}
