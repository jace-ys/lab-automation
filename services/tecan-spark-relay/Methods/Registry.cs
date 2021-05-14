using System.Collections.Generic;

using Fluid;

namespace TecanSparkRelay.Methods
{
    public class Registry
    {
        private readonly static Dictionary<string, SparkMethod> methods = new Dictionary<string, SparkMethod>
        {
            ["MeasureOD"] = new MeasureOD(),
        };

        static Registry()
        {
            TemplateContext.GlobalMemberAccessStrategy.Register<Plate>();
            TemplateContext.GlobalMemberAccessStrategy.Register<Well>();

            foreach (var (methodName, method) in methods)
            {
                method.Register(methodName);
                TemplateContext.GlobalMemberAccessStrategy.Register(method.SpecType());
            }
        }

        public static SparkMethod GetMethod(string methodName)
        {
            return methods[methodName];
        }
    }
}
