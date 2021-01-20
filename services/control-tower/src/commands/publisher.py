import queue
import threading


class CommandPublisher(threading.Thread):
    def __init__(self, logger, pubusb, queue=None, done=None):
        super(CommandPublisher, self).__init__()

        self.logger = logger
        self.pubsub = pubsub
        self.queue = queue
        self.done = done

    def run(self):
        while not self.done.is_set():
            try:
                command = self.queue.get(block=False)
                self.publish(command)

                self.logger.info(
                    "command.published",
                    channel=command.apiVersion,
                    command=command.json(),
                )

            except queue.Empty:
                pass

            except Exception as err:
                self.logger.error("command.publish.failed", error=err)
                raise

    def publish(self, command):
        self.pubsub.publish(command.apiVersion, command.json())
