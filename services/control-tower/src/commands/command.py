import json
import re
import uuid


class Command:
    def __init__(self, api_version, protocol, spec=None):
        if re.match(r"(?i)[a-z0-9-]+\/v[1-9]+[a-z0-9]*", api_version) is None:
            raise InvalidAPIVersion

        self.uuid = uuid.uuid4().hex[:16]
        self.apiVersion = api_version
        self.protocol = protocol
        self.spec = spec or {}

    def metadata(self, source, spec=None):
        self.metadata = {"source": {"name": source, "spec": spec or {}}}

    def json(self):
        return json.dumps(self, cls=CommandEncoder)


class CommandEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


class InvalidAPIVersion(Exception):
    pass
