from src.protocols.config import BaseConfig, ConfigType


class Config(BaseConfig):
    def schema():
        return {
            "tiprack": {
                "name": {
                    "type": ConfigType.labware,
                },
                "location": {
                    "type": ConfigType.location,
                },
            },
            "plate": {
                "name": {
                    "type": ConfigType.labware,
                },
                "location": {
                    "type": ConfigType.location,
                },
            },
            "reservoir": {
                "name": {
                    "type": ConfigType.labware,
                },
                "location": {
                    "type": ConfigType.location,
                },
            },
            "pipette": {
                "name": {
                    "type": ConfigType.instrument,
                },
                "mount": {
                    "type": ConfigType.mount,
                },
            },
        }
