using System;

namespace TecanSparkRelay.Protocols
{
    public class MeasureAbsorbance : Protocol
    {
        public MeasureAbsorbance() : base() { }

        public override void Validate()
        {
            base.Validate();
            var spec = (MeasureAbsorbanceSpec)this.SpecContext();

            if (spec.cycles <= 0)
            {
                throw new ApplicationException("number of cycles must be a positive value");
            }

            if (spec.shakingDuration <= 0)
            {
                throw new ApplicationException("shaking duration must be a positive value");
            }

            if (spec.measurementWavelength <= 0)
            {
                throw new ApplicationException("measurement wavelength must be a positive value");
            }
        }

        public override object SpecContext()
        {
            return this.wells[0];
        }

        public override Type SpecType()
        {
            return typeof(MeasureAbsorbanceSpec);
        }

        public override int Rows()
        {
            return 8;
        }

        public override int Columns()
        {
            return 12;
        }
    }

    public class MeasureAbsorbanceSpec
    {
        public int cycles { get; set; }
        public int measurementWavelength { get; set; }
        public int shakingDuration { get; set; }
    }
}
