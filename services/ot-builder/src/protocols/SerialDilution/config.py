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
            "trough": {
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
            "tube_rack": {
                "load_name": {
                    "type": ConfigType.labware,
                },
                "location": {
                    "type": ConfigType.location,
                },
            },
            "right_pipette": {
                "instrument_name": {
                    "type": ConfigType.instrument,
                }
            },
            "left_pipette": {
                "instrument_name": {
                    "type": ConfigType.instrument,
                }
            },
            "new_tip": {
                "strategy": {
                    "type": ConfigType.strategy,
                }
            },
        }
