using System;
using System.Collections.Generic;
using System.Threading;

using Tecan.At.Dragonfly.AutomationInterface.Data;

namespace TecanSparkRelay.System
{
    public interface AutomationInterface
    {
        IReadOnlyCollection<Instrument> GetInstruments();
        bool CheckMethod(Instrument selectedInstrument, string methodAsXml, string methodName, out IEnumerable<string> messages);
        MethodExecutionResult ExecuteMethod(Instrument selectedInstrument, string methodAsXml, string methodName, bool isStacker);
        string GetResults(Guid workspaceId, Guid executionId);
        string GetMethodXml(string methodName);
    }

    public class FakeAutomationInterface : AutomationInterface
    {
        private string methodName;

        public IReadOnlyCollection<Instrument> GetInstruments()
        {
            return new Instrument[] { new Instrument() };
        }

        public bool CheckMethod(Instrument selectedInstrument, string methodAsXml, string methodName, out IEnumerable<string> messages)
        {
            messages = null;
            return true;
        }

        public MethodExecutionResult ExecuteMethod(Instrument selectedInstrument, string methodAsXml, string methodName, bool isStacker)
        {
            this.methodName = methodName;

            for (var i = 0; i < 10; i++)
            {
                Console.WriteLine($"Executing method {methodName} using instrument {selectedInstrument.SerialNumber}: {i}");
                Thread.Sleep(1000);
            }

            Console.WriteLine($"Finished executing method {methodName} using instrument {selectedInstrument.SerialNumber}");

            return new MethodExecutionResult();
        }

        public string GetResults(Guid workspaceId, Guid executionId)
        {
            return $"./Protocols/{this.methodName}/Export.xml";
        }

        public string GetMethodXml(string methodName)
        {
            throw new NotImplementedException();
        }
    }

    public class Instrument
    {
        public readonly string SerialNumber;
        public readonly InstrumentState State = InstrumentState.FullyOperational;

        public Instrument()
        {
            this.SerialNumber = "1910012500";
        }
    }

    public class MethodExecutionResult
    {
        public readonly Guid WorkspaceId;
        public readonly Guid ExecutionId;

        public MethodExecutionResult()
        {
            this.WorkspaceId = new Guid();
            this.ExecutionId = new Guid();
        }
    }
}
