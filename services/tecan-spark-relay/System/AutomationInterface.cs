using System;
using System.Collections.Generic;
using System.Threading;

namespace TecanSparkRelay.System
{
  public interface AutomationInterface
  {
    IReadOnlyCollection<int> GetInstruments();
    (Guid, Guid) ExecuteMethod(int selectedInstrument, string methodAsXml, string methodName, bool isStacker);
    string GetResults(Guid workspaceId, Guid executionId);
  }

  public class FakeAutomationInterface : AutomationInterface
  {
    private string methodName;

    public IReadOnlyCollection<int> GetInstruments()
    {
      return new int[] { 1870244653, 1910012500 };
    }

    public (Guid, Guid) ExecuteMethod(int selectedInstrument, string methodAsXml, string methodName, bool isStacker)
    {
      this.methodName = methodName;

      for (var i = 0; i < 10; i++)
      {
        Console.WriteLine($"Executing method {methodName} using instrument {selectedInstrument}: {i}");
        Thread.Sleep(1000);
      }

      Console.WriteLine($"Finished executing method {methodName} using instrument {selectedInstrument}");

      return (new Guid(), new Guid());
    }

    public string GetResults(Guid workspaceId, Guid executionId)
    {
      return $"./Methods/{this.methodName}/Export.xml";
    }
  }
}
