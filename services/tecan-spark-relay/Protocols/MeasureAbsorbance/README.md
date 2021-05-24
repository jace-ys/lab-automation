# `MeasureAbsorbance`

This protocol uses the plate reader to perform an absorbance measurement under the given specifications.

## Spec

This protocol is a plate-based protocol and thus expects a list of `spec` objects containing the following parameters:

- `cycles (int)`: number of kinetic loop cycles
- `measurementWavelength (int)`: wavelength to use for absorbance measurement in _nm_
- `shakingDuration (int)`: number of seconds to shake for

However, as the Spark® performs the same method on all wells, the `spec` of the first well is used and applied to all the other selected wells. The `spec` of the other wells are ignored.
