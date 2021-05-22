# `PlateTransfer`

This protocol transfers the specified volumes from wells on a source plate to their
corresponding wells on a destination plate.

## Spec

This protocol is a plate-based protocol and thus expects a list of `spec` objects containing the following parameters:

- `volume (int)`: amount in uL to transfer from the source plate to the corresponding well in the destination plate
