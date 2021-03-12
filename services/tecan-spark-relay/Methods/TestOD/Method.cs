using System;

namespace TecanSparkRelay.Methods
{
    public class TestOD : SparkMethod
    {
        public int shakingDuration { get; set; }

        public TestOD() : base() { }

        public override void Validate()
        {
            if (this.shakingDuration <= 0)
            {
                throw new ApplicationException("shaking duration must be a positive value");
            }
        }
    }
}
