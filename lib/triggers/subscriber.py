import json

from lib import log

logger = log.Logger.new()


class Subscriber:
    def __init__(self, handler):
        self.handler = handler

    def receive(self, message):
        if message["type"] == "message":
            logger.info("trigger.received", trigger=message["data"])
            trigger = json.loads(message["data"])
            self.handler.handle_trigger(trigger)
