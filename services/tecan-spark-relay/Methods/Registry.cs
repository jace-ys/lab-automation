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

            foreach (KeyValuePair<string, SparkMethod> kvp in methods)
            {
                var methodName = kvp.Key;
                var method = kvp.Value;

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
