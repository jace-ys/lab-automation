using System;

namespace TecanSparkRelay.Methods
{
    public class TestOD : SparkMethod
    {
        public TestOD() : base() { }

        public override void Validate()
        {
            base.Validate();

            var spec = (TestODSpec)this.SpecContext();
            if (spec.shakingDuration <= 0)
            {
                throw new ApplicationException("shaking duration must be a positive value");
            }
        }

        public override object SpecContext()
        {
            return this.wells[0];
        }

        public override Type SpecType()
        {
            return typeof(TestODSpec);
        }
    }

    public class TestODSpec
    {
        public int shakingDuration { get; set; }
    }
}
