class Data:
    def __init__(self, row=None):
        if row:
            # Split the CSV data row
            data = row.split(",", 46)
        else:
            # Set to empty string
            data = [""] * 47

        # Assign the data accordingly
        (
            self.timeElapsed,
            self.odMeasured,
            self.odSetpoint,
            self.odZeroSetpoint,
            self.thermostatSetpoint,
            self.heatingRate,
            self.internalAirTemp,
            self.externalAirTemp,
            self.mediaTemp,
            self.optGenActInt,
            self.pump1Rate,
            self.pump2Rate,
            self.pump3Rate,
            self.pump4Rate,
            self.mediaVol,
            self.stirringRate,
            self.led395NmSetpoint,
            self.led457NmSetpoint,
            self.led500NmSetpoint,
            self.led523NmSetpoint,
            self.led595NmSetpoint,
            self.led623NmSetpoint,
            self.led6500KSetpoint,
            self.laserSetpoint,
            self.ledUvInt,
            self.fp1Base,
            self.fp1Emit1,
            self.fp1Emit2,
            self.fp1Emit1Raw,
            self.fp1Emit2Raw,
            self.fp2Base,
            self.fp2Emit1,
            self.fp2Emit2,
            self.fp2Emit1Raw,
            self.fp2Emit2Raw,
            self.fp3Base,
            self.fp3Emit1,
            self.fp3Emit2,
            self.fp3Emit1Raw,
            self.fp3Emit2Raw,
            self.customProgParam1,
            self.customProgParam2,
            self.customProgParam3,
            self.customProgStatus,
            self.zigzagTarget,
            self.growthRate,
            self.odRaw,
        ) = data
        self.error = None


class DataRow:
    def __init__(self, data: Data):
        self.data = vars(data)
