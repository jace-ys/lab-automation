from opentrons import protocol_api

# spec:
#     - volume

metadata = {
    "protocolName": "OT-2/v1alpha1/SimpleDilution",
    "apiLevel": "2.7",
}


def describe():
    return """
This protocol performs a simple dilution by adding specified volumes of a diluent from
a reservoir to wells on a destination plate.
"""


def run(protocol: protocol_api.ProtocolContext):
    tiprack = protocol.load_labware(**config["tiprack"])
    pipette = protocol.load_instrument(**config["pipette"], tip_racks=[tiprack])

    # Plate containing solution to be diluted
    plate = protocol.load_labware(**config["plate"])
    # Reservoir containing diluent
    reservoir = protocol.load_labware(**config["reservoir"])

    pipette.distribute(
        volume=list(map(lambda well: well["volume"], spec)),
        source=reservoir["A1"],
        dest=plate.wells()[: len(spec)],
    )
