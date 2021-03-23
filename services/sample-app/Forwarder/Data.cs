using System;

namespace TecanSparkRelay.Forwarder
{
    public class Data
    {
        public double expTime;
        public string error;

        public void Error(Exception ex)
        {
            this.error = ex.Message;
        }
    }
}
