import json
import queue
import threading


class TriggerPublisher(threading.Thread):
    def __init__(self, logger, cache, pubsub, cfg, queue=None, done=None):
        super(TriggerPublisher, self).__init__()

        self.logger = logger
        self.cache = cache
        self.pubsub = pubsub
        self.queue = queue
        self.done = done
        self.cache_key = cfg.CACHE_KEY

    def run(self):
        # Keep polling the queue until a done signal is received
        while not self.done.is_set():
            try:
                trigger = self.queue.get(block=False)
                # Publish the trigger
                self.publish(trigger)
                self.logger.info(
                    "trigger.published",
                    topic=trigger.apiVersion,
                    trigger=trigger.json(),
                )

            except queue.Empty:
                pass

            except Exception as err:
                self.logger.error("trigger.publish.failed", error=err)

    def publish(self, trigger):
        # Add the trigger to the cache for tracking
        self.create(trigger)
        self.pubsub.publish(trigger.apiVersion, trigger.json())

    def get(self, uuid):
        trigger = self.cache.hget(self.cache_key, uuid)
        if trigger is None:
            raise ValueError(f"could not find trigger with UUID {uuid}")

        return json.loads(trigger)

    def create(self, trigger):
        self.cache.hset(self.cache_key, trigger.uuid, trigger.json())
