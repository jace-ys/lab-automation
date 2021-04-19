using System;

namespace TecanSparkRelay.Methods
{
    public class MeasureOD : SparkMethod
    {
        public MeasureOD() : base() { }

        public override void Validate()
        {
            base.Validate();

            var spec = (MeasureODSpec)this.SpecContext();
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
            return typeof(MeasureODSpec);
        }
    }

    public class MeasureODSpec
    {
        public int shakingDuration { get; set; }
    }
}
