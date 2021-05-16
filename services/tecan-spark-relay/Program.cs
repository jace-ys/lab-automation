using System;
using System.Threading;

using CommandLine;
using Serilog;
using Serilog.Formatting.Compact;
using ServiceStack.Redis;

namespace TecanSparkRelay
{
    class Program
    {
        [Verb("server", HelpText = "Run the server.")]
        public class ServerOptions { }

        [Verb("export", HelpText = "Run the export utility.")]
        public class ExportOptions
        {
            [Option("method", Required = true, HelpText = "Name of the method to export to XML.")]
            public string MethodName { get; set; }
        }

        static void Main(string[] args)
        {
            Parser.Default.ParseArguments<ServerOptions, ExportOptions>(args)
                .WithParsed<ServerOptions>(options => RunServer())
                .WithParsed<ExportOptions>(options => RunExport(options.MethodName))
                .WithNotParsed(errors => Console.WriteLine(errors));
        }

        static void RunServer()
        {
            var cfg = new Config();
            var logger = new LoggerConfiguration().WriteTo.Console(new CompactJsonFormatter()).CreateLogger();

            var redis = new RedisClient(cfg.pubsub.URL);
            var forwarder = new Forwarder.Forwarder(cfg.forwarder);

            var topic = cfg.version;
            if (!String.IsNullOrEmpty(cfg.manager.DeviceName))
            {
                topic += $"/{cfg.manager.DeviceName}";
            }

            System.Manager.Init();
            var manager = new System.Manager(logger, forwarder, redis, topic, cfg.manager);
            var subscribe = new Thread(new ThreadStart(manager.Subscribe));

            subscribe.Start();
            logger.Information("manager.subscribe.started {topic}", topic);

            Console.CancelKeyPress += new ConsoleCancelEventHandler((sender, e) =>
            {
                manager.Shutdown();
                logger.Information("managed.subscribe.stopped");
            });

            subscribe.Join();
        }

        static void RunExport(string methodName)
        {
            System.Manager.Init();
            var methodXML = System.Manager.ExportMethod(methodName);

            if (String.IsNullOrEmpty(methodXML))
            {
                Console.WriteLine($"Could not find a method named {methodName}");
            }
            else
            {
                Console.WriteLine(methodXML);
            }
        }
    }
}
