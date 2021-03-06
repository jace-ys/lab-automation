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
            "plate": {
                "hint": "Plate containing the solution to be diluted",
                "spec": {
                    "load_name": ConfigType.labware,
                    "location": ConfigType.location,
                },
            },
            "reservoir": {
                "hint": "Reservoir containing the diluent",
                "spec": {
                    "load_name": ConfigType.labware,
                    "location": ConfigType.location,
                },
            },
        }
