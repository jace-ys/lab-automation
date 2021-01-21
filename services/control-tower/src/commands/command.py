import json
import uuid


class Command:
    def __init__(self, api_version, protocol, spec={}):
        if len(api_version.split("/v")) != 2:
            raise InvalidAPIVersion

        self.uuid = uuid.uuid4().hex[:16]
        self.apiVersion = api_version
        self.protocol = protocol
        self.spec = spec

    def with_metadata(self, source, spec={}):
        self.metadata = {"source": {"name": source, "spec": spec}}
        return self

    def json(self):
        return json.dumps(self, cls=CommandEncoder)


class CommandEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


class InvalidAPIVersion(Exception):
    pass
