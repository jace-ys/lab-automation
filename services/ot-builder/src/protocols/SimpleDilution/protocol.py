from opentrons import protocol_api

# spec:
#     water:
#         volume
#     reagent:
#         volume

metadata = {
    "protocolName": "OT-2/v1alpha1/SimpleDilution",
    "apiLevel": "2.7",
}


def run(protocol: protocol_api.ProtocolContext):
    tiprack = protocol.load_labware(**config["tiprick"])
    plate = protocol.load_labware(**config["plate"])
    reservoir = protocol.load_labware(**config["reservoir"])
    pipette = protocol.load_instrument(**config["pipette"], tip_racks=[tiprack])

    reagent = reservoir["A1"]
    water = reservoir["A12"]
    dest = plate.rows()[0]

    pipette.distribute(spec["reagent"]["volume"], reagent, dest)
    pipette.distribute(
        spec["water"]["volume"],
        water,
        dest,
        mix_after=(3, spec["water"]["volume"] / 2),
    )
