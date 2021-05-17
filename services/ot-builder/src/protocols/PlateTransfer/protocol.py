from opentrons import protocol_api

# spec:
#     - volume

metadata = {
    "protocolName": "OT-2/v1alpha1/PlateTransfer",
    "apiLevel": "2.7",
}


def describe():
    return """
This protocol transfers the specified volumes from wells on a source plate to their
corresponding wells on a destination plate.
"""


def run(protocol: protocol_api.ProtocolContext):
    tiprack = protocol.load_labware(**config["tiprack"])
    pipette = protocol.load_instrument(**config["pipette"], tip_racks=[tiprack])

    # Plate to transfer from
    source = protocol.load_labware(**config["source"])
    # Plate to transfer to
    destination = protocol.load_labware(**config["destination"])

    for (index, well) in enumerate(spec):
        volume = well["volume"]
        pipette.transfer(
            volume=volume,
            source=source.wells()[index],
            dest=destination.wells()[index],
            new_tip="always",
            mix_after=(3, volume / 2),
        )
