from opentrons import protocol_api

# spec:
#     base:
#         dilutionFactor
#         numOfDilutions
#         totalMixingVolume
#         initialVolume

metadata = {
    "protocolName": "OT-2/v1alpha1/SerialDilution",
    "apiLevel": "2.7",
}


def run(protocol: protocol_api.ProtocolContext):
    dilution_factor = spec["dilutionFactor"]
    num_of_dilutions = spec["numOfDilutions"]
    total_mixing_volume = spec["totalMixingVolume"]
    initial_volume = spec["initialVolume"]

    # labware
    trough = protocol.load_labware(**config["trough"])
    liquid_trash = trough.wells()[0]
    plate = protocol.load_labware(**config["plate"])
    tipracks = [
        protocol.load_labware(config["tiprack"]["load_name"], slot)
        for slot in config["tiprack"]["location"]
    ]

    sample_tubes = protocol.load_labware(**config["tube_rack"])

    pipette = protocol.load_instrument(
        **config["right_pipette"], mount="right", tip_racks=tipracks
    )

    pipette_left = protocol.load_instrument(
        **config["left_pipette"], mount="left", tip_racks=tipracks
    )

    transfer_volume = total_mixing_volume / dilution_factor
    diluent_volume = total_mixing_volume - transfer_volume

    pipette_left.pick_up_tip(tipracks[0]["A12"])
    # part 1 transfer food dye to the wells
    pipette_left.transfer(
        volume=initial_volume,
        source=sample_tubes.wells("A1"),
        dest=plate.columns("1"),
        liquid_trash=liquid_trash,
        new_tip=config["new_tip"]["strategy"],
    )
    pipette_left.drop_tip()

    # part 2 serial dilution
    if "multi" in config["right_pipette"]["instrument_name"]:
        # Distribute diluent across the plate to the the number of samples
        # And add diluent to one column after the number of samples for a blank
        pipette.transfer(
            diluent_volume, trough.wells()[0], plate.rows()[0][1 : 1 + num_of_dilutions]
        )

        # Dilution of samples across the 96-well flat bottom plate
        pipette.pick_up_tip()

        for s, d in zip(
            plate.rows()[0][:num_of_dilutions],
            plate.rows()[0][1 : 1 + num_of_dilutions],
        ):
            pipette.transfer(
                transfer_volume,
                s,
                d,
                mix_after=(3, total_mixing_volume / 2),
                new_tip=config["new_tip"]["strategy"],
            )

        # Remove transfer volume from the last column of the dilution
        pipette.transfer(
            transfer_volume,
            plate.rows()[0][num_of_dilutions],
            liquid_trash,
            new_tip=config["new_tip"]["strategy"],
            blow_out=True,
        )

        if config["new_tip"]["strategy"] == "never":
            pipette.drop_tip()

    else:
        # Distribute diluent across the plate to the the number of samples
        # And add diluent to one column after the number of samples for a blank
        for col in plate.columns()[1 : 1 + num_of_dilutions]:
            pipette.distribute(
                diluent_volume, trough.wells()[0], [well for well in col]
            )

        for row in plate.rows():
            if config["new_tip"]["strategy"] == "never":
                pipette.pick_up_tip()

            for s, d in zip(row[:num_of_dilutions], row[1 : 1 + num_of_dilutions]):

                pipette.transfer(
                    transfer_volume,
                    s,
                    d,
                    mix_after=(3, total_mixing_volume / 2),
                    new_tip=config["new_tip"]["strategy"],
                )

                pipette.transfer(
                    transfer_volume,
                    row[num_of_dilutions],
                    liquid_trash,
                    new_tip=config["new_tip"]["strategy"],
                    blow_out=True,
                )

            if config["new_tip"]["strategy"] == "never":
                pipette.drop_tip()
