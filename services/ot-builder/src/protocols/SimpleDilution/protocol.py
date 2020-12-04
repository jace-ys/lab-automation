from opentrons import protocol_api

metadata = {
    "protocolName": "OT-2/v1alpha1/SimpleDilution",
    "apiLevel": "2.7",
}


def run(protocol: protocol_api.ProtocolContext):
    tiprack = protocol.load_labware(
        load_name=spec["tiprack"]["name"],
        location=spec["tiprack"]["location"],
    )

    plate = protocol.load_labware(
        load_name=spec["plate"]["name"],
        location=spec["plate"]["location"],
    )

    reservoir = protocol.load_labware(
        load_name=spec["reservoir"]["name"],
        location=spec["reservoir"]["location"],
    )

    pipette = protocol.load_instrument(
        instrument_name=spec["pipette"]["name"],
        mount=spec["pipette"]["mount"],
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
