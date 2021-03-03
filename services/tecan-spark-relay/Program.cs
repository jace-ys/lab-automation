using System;
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

      var redis = new RedisClient(cfg.pubsub.ADDR);
      System.AutomationInterface ai = new System.FakeAutomationInterface();

      var manager = new System.Manager(logger, ai, redis, cfg.pubsub.SUBSCRIPTION_TOPIC, cfg.manager);
      var subscribe = new Thread(new ThreadStart(manager.Subscribe));

      subscribe.Start();
      logger.Information("manager.subscribe.started");

      Console.CancelKeyPress += new ConsoleCancelEventHandler((sender, e) =>
      {
        logger.Information("service.teardown");
        manager.Unsubscribe();
      });

      subscribe.Join();
      logger.Information("managed.subscribe.stopped");
    }
  }
}
