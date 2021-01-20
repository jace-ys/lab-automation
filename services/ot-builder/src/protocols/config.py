from enum import Enum

ConfigType = Enum("ConfigType", ["labware", "location", "instrument", "mount"])


class BaseConfig:
    def schema():
        return NotImplemented
