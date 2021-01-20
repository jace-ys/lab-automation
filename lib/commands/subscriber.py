import json

from lib import log

logger = log.Logger.new()


class Subscriber:
    def __init__(self, handler):
        self.handler = handler

    def receive(self, message):
        if message["type"] == "message":
            logger.info("command.received", command=message["data"])
            command = json.loads(message["data"])
            self.handler.handle_command(command)
