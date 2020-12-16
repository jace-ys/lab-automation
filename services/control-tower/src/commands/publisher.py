import queue
import threading


class CommandPublisher(threading.Thread):
    def __init__(self, logger, redis, queue, done):
        super(CommandPublisher, self).__init__()

        self.logger = logger
        self.redis = redis
        self.queue = queue
        self.done = done

    def run(self):
        while not self.done.is_set():
            try:
                command = self.queue.get(block=False)
                self.publish(command)

            except queue.Empty:
                pass

    def publish(self, command):
        self.redis.publish(command.apiVersion, command.json())

        self.logger.info(
            "command.published",
            channel=command.apiVersion,
            command=command.json(),
        )
