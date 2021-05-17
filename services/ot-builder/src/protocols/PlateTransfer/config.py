from src.protocols.config import BaseConfig, ConfigType


class Config(BaseConfig):
    def schema():
        return {
            "tiprack": {
                "spec": {
                    "load_name": ConfigType.labware,
                    "location": ConfigType.location,
                }
            },
            "pipette": {
                "spec": {
                    "instrument_name": ConfigType.instrument,
                    "mount": ConfigType.mount,
                }
            },
            "source": {
                "hint": "Plate to transfer the solution from",
                "spec": {
                    "load_name": ConfigType.labware,
                    "location": ConfigType.location,
                },
            },
            "destination": {
                "hint": "Plate to transfer the solution to",
                "spec": {
                    "load_name": ConfigType.labware,
                    "location": ConfigType.location,
                },
            },
        }
