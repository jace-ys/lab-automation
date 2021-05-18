using System;
using System.Collections.Generic;

using Fluid;

namespace TecanSparkRelay.Methods
{
    public class Registry
    {
        private readonly static Dictionary<string, Type> methods = new Dictionary<string, Type>
        {
            ["MeasureAbsorbance"] = typeof(MeasureAbsorbance),
        };

        static Registry()
        {
            TemplateContext.GlobalMemberAccessStrategy.Register<Plate>();
            TemplateContext.GlobalMemberAccessStrategy.Register<Well>();

            foreach (var methodName in methods.Keys)
            {
                var method = GetMethod(methodName);
                method.Register(methodName);
                TemplateContext.GlobalMemberAccessStrategy.Register(method.SpecType());
            }
        }

        public static SparkMethod GetMethod(string methodName)
        {
            return (SparkMethod)Activator.CreateInstance(methods[methodName], new object[] { });
        }
    }
}
