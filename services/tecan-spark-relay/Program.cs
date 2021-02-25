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
      var context = new CancellationTokenSource();

      var redis = new RedisClient(cfg.pubsubAddr);

      var manager = new Manager(logger, redis, cfg.pubsubSubscriptionTopic);
      var forwarder = new Forwarder(logger, context.Token);

      var subscribe = new Thread(new ThreadStart(manager.Subscribe));
      var forward = new Thread(new ThreadStart(forwarder.Run));

      subscribe.Start();
      forward.Start();

      Console.CancelKeyPress += new ConsoleCancelEventHandler((sender, e) =>
      {
        logger.Information("service.teardown");
        context.Cancel();
        manager.Unsubscribe();
      });

      subscribe.Join();
      logger.Information("pubsub.listen.stopped");

      forward.Join();
      logger.Information("data.forwarder.stopped");
    }
  }
}
