import json
import uuid


class CommandEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


class Command:
    def __init__(self, api_version, protocol):
        self.uuid = uuid.uuid4().hex[:16]
        self.apiVersion = api_version
        self.protocol = protocol
        self.spec = {}

    def json(self):
        return json.dumps(self, indent=4, cls=CommandEncoder)
