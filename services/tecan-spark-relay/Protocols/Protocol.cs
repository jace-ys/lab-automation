using System;
using System.Collections.Generic;
using System.IO;

using Fluid;

namespace TecanSparkRelay.Protocols
{
    // Abstract class that all protocols should inherit from
    public abstract class Protocol
    {
        public List<object> wells = new List<object>();
        private static IFluidTemplate templateXML;

        public void Register(string protocolName)
        {
            // Parse the templated method XML file for each protocol and register it
            var template = File.ReadAllText($"./Protocols/{protocolName}/Method.xml");
            templateXML = FluidTemplate.Parse(template);
        }

        public virtual string GenerateMethodXML()
        {
            // Generate the method XML file using the provided plate and spec
            var context = new { plate = this.Plate(), spec = this.SpecContext() };
            return templateXML.Render(new TemplateContext(context));
        }

        public virtual void Validate()
        {
            // Check that the provided spec matches the expected spec for the protocol
            Type type = this.SpecType();
            if (this.SpecContext().GetType() != type)
            {
                throw new ApplicationException($"spec is not of type {type}");
            };
        }

        public virtual object SpecContext()
        {
            // Return a spec object for populating the method XML template
            return this;
        }

        public virtual Type SpecType()
        {
            throw new NotImplementedException();
        }

        public Plate Plate()
        {
            // Use the number of selected wells to generate the plate configuration
            return new Plate(this.Rows(), this.Columns(), this.wells.Count);
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
