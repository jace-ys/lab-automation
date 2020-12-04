class Schema:
    def __init__(self):
        self.spec = {
            "reagent": {"volume": {"type": "int"}},
            "water": {"volume": {"type": "int"}},
            "local": {
                "tiprack": {
                    "name": {
                        "type": "labware",
                    },
                    "location": {
                        "type": "location",
                    },
                },
                "plate": {
                    "name": {
                        "type": "labware",
                    },
                    "location": {
                        "type": "location",
                    },
                },
                "reservoir": {
                    "name": {
                        "type": "labware",
                    },
                    "location": {
                        "type": "location",
                    },
                },
                "pipette": {
                    "name": {
                        "type": "instrument",
                    },
                    "mount": {
                        "type": "mount",
                    },
                },
            },
        }

    def validate(self, run):
        undefined = {}

        for k, v in self.spec.items():
            if k not in run["spec"]:
                undefined[k] = v

        return undefined
