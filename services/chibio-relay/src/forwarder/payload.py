class Data:
    def __init__(self, row=None):
        if row:
            data = row.split(",", 40)
        else:
            data = [""] * 40

        self.expTime = data[0]
        self.odMeasured = data[1]
        self.odSetpoint = data[2]
        self.odZeroSetpoint = data[3]
        self.thermostatSetpoint = data[4]
        self.heatingRate = data[5]
        self.internalAirTemp = data[6]
        self.externalAirTemp = data[0]
        self.mediaTemp = data[7]
        self.optGenActInt = data[8]
        self.pump1Rate = data[9]
        self.pump2Rate = data[10]
        self.pump3Rate = data[11]
        self.pump4Rate = data[12]
        self.mediaVol = data[13]
        self.stirringRate = data[14]
        self.LED395NmSetpoint = data[15]
        self.LED457NmSetpoint = data[16]
        self.LED500NmSetpoint = data[17]
        self.LED523NmSetpoint = data[18]
        self.LED595NmSetpoint = data[19]
        self.LED623NmSetpoint = data[20]
        self.LED6500KSetpoint = data[21]
        self.laserSetpoint = data[22]
        self.LEDUVInt = data[23]
        self.FP1Base = data[24]
        self.FP1Emit1 = data[25]
        self.FP1Emit2 = data[26]
        self.FP2Base = data[27]
        self.FP2Emit1 = data[28]
        self.FP2Emit2 = data[29]
        self.FP3Base = data[30]
        self.FP3Emit1 = data[31]
        self.FP3Emit2 = data[32]
        self.customProgParam1 = data[33]
        self.customProgParam2 = data[34]
        self.customProgParam3 = data[35]
        self.customProgPtatus = data[37]
        self.zigzagTarget = data[38]
        self.growthRate = data[39]
        self.error = ""


class DataRow:
    def __init__(self, data: Data):
        self.data = vars(data)
