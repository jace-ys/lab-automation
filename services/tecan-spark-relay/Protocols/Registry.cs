using System;
using System.Collections.Generic;

using Fluid;

namespace TecanSparkRelay.Protocols
{
    public class Registry
    {
        private readonly static Dictionary<string, Type> protocols = new Dictionary<string, Type>
        {
            ["MeasureAbsorbance"] = typeof(MeasureAbsorbance),
        };

        static Registry()
        {
            TemplateContext.GlobalMemberAccessStrategy.Register<Plate>();
            TemplateContext.GlobalMemberAccessStrategy.Register<Well>();

            foreach (var protocolName in protocols.Keys)
            {
                // Register each protocol
                var protocol = GetProtocol(protocolName);
                protocol.Register(protocolName);
                TemplateContext.GlobalMemberAccessStrategy.Register(protocol.SpecType());
            }
        }

        public static Protocol GetProtocol(string protocol)
        {
            return (Protocol)Activator.CreateInstance(protocols[protocol], new object[] { });
        }
    }
}
