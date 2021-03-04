from src.protocols.config import BaseConfig, ConfigType


class Config(BaseConfig):
    def schema():
        return {
            "tiprack": {
                "load_name": {
                    "type": ConfigType.labware,
                },
                "location": {
                    "type": ConfigType.location,
                },
            },
            "plate": {
                "load_name": {
                    "type": ConfigType.labware,
                },
                "location": {
                    "type": ConfigType.location,
                },
            },
            "reservoir": {
                "load_name": {
                    "type": ConfigType.labware,
                },
                "location": {
                    "type": ConfigType.location,
                },
            },
            "pipette": {
                "instrument_name": {
                    "type": ConfigType.instrument,
                },
                "mount": {
                    "type": ConfigType.mount,
                },
            },
        }
