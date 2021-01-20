from opentrons import protocol_api

metadata = {
    "protocolName": "OT-2/v1alpha1/SimpleDilution",
    "apiLevel": "2.7",
}


def run(protocol: protocol_api.ProtocolContext):
    tiprack = protocol.load_labware(
        load_name=config["tiprack"]["name"],
        location=config["tiprack"]["location"],
    )

    plate = protocol.load_labware(
        load_name=config["plate"]["name"],
        location=config["plate"]["location"],
    )

    reservoir = protocol.load_labware(
        load_name=config["reservoir"]["name"],
        location=config["reservoir"]["location"],
    )

    pipette = protocol.load_instrument(
        instrument_name=config["pipette"]["name"],
        mount=config["pipette"]["mount"],
        tip_racks=[tiprack],
    )

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
