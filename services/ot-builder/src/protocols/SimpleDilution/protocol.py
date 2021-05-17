from opentrons import protocol_api

# spec:
#     - volume

metadata = {
    "protocolName": "OT-2/v1alpha1/SimpleDilution",
    "apiLevel": "2.7",
}


def run(protocol: protocol_api.ProtocolContext):
    tiprack = protocol.load_labware(**config["tiprack"])
    plate = protocol.load_labware(**config["plate"])
    reservoir = protocol.load_labware(**config["reservoir"])
    pipette = protocol.load_instrument(**config["pipette"], tip_racks=[tiprack])

    dilutant = reservoir["A1g"]
    volumes = list(map(lambda well: well["volume"], spec))
    wells = plate.wells()[: len(volumes)]

    pipette.distribute(volumes, dilutant, wells, mix_after=(3, 10))
