import json
import queue
import threading


class CommandPublisher(threading.Thread):
    def __init__(self, logger, cache, pubsub, cfg, queue=None, done=None):
        super(CommandPublisher, self).__init__()

        self.logger = logger
        self.cache = cache
        self.pubsub = pubsub
        self.queue = queue
        self.done = done
        self.cache_key = cfg.CACHE_KEY

    def run(self):
        while not self.done.is_set():
            try:
                command = self.queue.get(block=False)
                self.publish(command)
                self.logger.info(
                    "command.published",
                    topic=command.apiVersion,
                    command=command.json(),
                )

            except queue.Empty:
                pass

            except Exception as err:
                self.logger.error("command.publish.failed", error=err)

    def publish(self, command):
        self.create(command)
        self.pubsub.publish(command.apiVersion, command.json())

    def get(self, uuid):
        cmd = self.cache.hget(self.cache_key, uuid)
        if cmd is None:
            raise ValueError(f"could not find command with UUID {uuid}")

        return json.loads(cmd)

    def create(self, command):
        self.cache.hset(self.cache_key, command.uuid, command.json())
