using System;

namespace TecanSparkRelay.Methods
{
    public class TestMethod : SparkMethod
    {
        public TimeSpan waitTime { get; set; }

        public TestMethod() : base() { }

        public override void Validate()
        {
            Console.WriteLine(this.waitTime);
        }
    }
}
