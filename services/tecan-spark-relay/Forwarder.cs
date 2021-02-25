using System;
using System.Threading;

using Serilog;

namespace TecanSparkRelay
{
  public class Forwarder
  {
    private ILogger logger;
    private CancellationToken done;
    private int checkInterval = 10;

    public Forwarder(ILogger logger, CancellationToken done)
    {
      this.logger = logger;
      this.done = done;
    }

    public void Run()
    {
      while (true)
      {
        try
        {
          this.done.ThrowIfCancellationRequested();
        }
        catch (OperationCanceledException)
        {
          return;
        }

        this.logger.Information("batch.poll.started");
        Thread.Sleep(this.checkInterval * 1000);
      }
    }
  }
}
