using System.Collections.Generic;
using System.IO;

using Fluid;

namespace TecanSparkRelay.Methods
{

  public abstract class SparkMethod
  {
    public IFluidTemplate templateXML;

    public virtual void Register(string methodName)
    {
      var template = File.ReadAllText($"./Methods/{methodName}/Method.xml");
      templateXML = FluidTemplate.Parse(template);
    }

    public virtual string GenerateMethodXML()
    {
      var context = new TemplateContext(this);
      return templateXML.Render(context);
    }

    public abstract void Validate();
  }

  public class Registry
  {
    private readonly static Dictionary<string, SparkMethod> methods = new Dictionary<string, SparkMethod>
    {
      ["TestMethod"] = new TestMethod(),
    };

    static Registry()
    {
      foreach (var (methodName, method) in methods)
      {
        method.Register(methodName);
      }
    }

    public static SparkMethod GetMethod(string methodName)
    {
      return methods[methodName];
    }
  }
}
