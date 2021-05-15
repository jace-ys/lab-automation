using System;
using System.IO;
using System.Threading;

using Serilog;
using Serilog.Formatting.Compact;
using ServiceStack.Redis;

namespace TecanSparkRelay
{
    class Program
    {
        static void Main(string[] args)
        {
            var cfg = new Config();
            var logger = new LoggerConfiguration().WriteTo.Console(new CompactJsonFormatter()).CreateLogger();

            var redis = new RedisClient(cfg.pubsub.Addr);
            var forwarder = new Forwarder.Forwarder(cfg.forwarder);

            var topic = Path.Join(cfg.version, cfg.manager.DeviceName);
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
    }
}
