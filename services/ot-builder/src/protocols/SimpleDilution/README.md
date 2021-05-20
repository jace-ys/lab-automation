# `SimpleDilution`

This protocol performs a simple dilution by adding specified volumes of a diluent from
a reservoir to wells on a destination plate.

## Spec

This protocol is a well-based protocol and thus expects a list of `spec` objects containing the following parameters:

- `volume (int)`: amount of diluent in uL to add to the well in the destination plate
