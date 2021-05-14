using System;
using System.Collections.Generic;
using System.IO;

using Fluid;

namespace TecanSparkRelay.Methods
{
    public abstract class SparkMethod
    {
        public List<object> wells = new List<object>();
        private IFluidTemplate templateXML;

        public virtual void Register(string methodName)
        {
            var template = File.ReadAllText($"./Methods/{methodName}/Method.xml");
            templateXML = FluidTemplate.Parse(template);
        }

        public virtual string GenerateMethodXML()
        {
            var plate = new Plate(this.Rows(), this.Columns(), this.wells.Count);
            var context = new { plate = plate, spec = this.SpecContext() };
            return templateXML.Render(new TemplateContext(context));
        }

        public virtual void Validate()
        {
            Type type = this.SpecType();
            if (this.SpecContext().GetType() != type)
            {
                throw new ApplicationException($"spec is not of type {type}");
            };
        }

        public virtual object SpecContext()
        {
            return this;
        }

        public virtual Type SpecType()
        {
            throw new NotImplementedException();
        }

        public virtual int Rows()
        {
            return 0;
        }

        public virtual int Columns()
        {
            return 0;
        }
    }
}
