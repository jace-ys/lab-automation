from enum import Enum

ConfigType = Enum(
    "ConfigType",
    [
        "labware",
        "location",
        "instrument",
        "mount",
        "strategy",
    ],
)


class BaseConfig:
    def schema():
        return NotImplemented
