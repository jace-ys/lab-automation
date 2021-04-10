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
            var context = new TemplateContext(this.SpecContext());
            return templateXML.Render(context);
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
    }

    public class Registry
    {
        private readonly static Dictionary<string, SparkMethod> methods = new Dictionary<string, SparkMethod>
        {
            ["TestOD"] = new TestOD(),
        };

        static Registry()
        {
            foreach (KeyValuePair<string, SparkMethod> kvp in methods)
            {
                kvp.Value.Register(kvp.Key);
            }
        }

        public static SparkMethod GetMethod(string methodName)
        {
            return methods[methodName];
        }
    }
}
