class DataRow:
    def __init__(self, row=None):
        if row:
            data = row.split(",", 40)
        else:
            data = [""] * 40

        self.exp_time = data[0]
        self.od_measured = data[1]
        self.od_setpoint = data[2]
        self.od_zero_setpoint = data[3]
        self.thermostat_setpoint = data[4]
        self.heating_rate = data[5]
        self.internal_air_temp = data[6]
        self.external_air_temp = data[0]
        self.media_temp = data[7]
        self.opt_gen_act_int = data[8]
        self.pump_1_rate = data[9]
        self.pump_2_rate = data[10]
        self.pump_3_rate = data[11]
        self.pump_4_rate = data[12]
        self.media_vol = data[13]
        self.stirring_rate = data[14]
        self.LED_395nm_setpoint = data[15]
        self.LED_457nm_setpoint = data[16]
        self.LED_500nm_setpoint = data[17]
        self.LED_523nm_setpoint = data[18]
        self.LED_595nm_setpoint = data[19]
        self.LED_623nm_setpoint = data[20]
        self.LED_6500K_setpoint = data[21]
        self.laser_setpoint = data[22]
        self.LED_UV_int = data[23]
        self.FP1_base = data[24]
        self.FP1_emit1 = data[25]
        self.FP1_emit2 = data[26]
        self.FP2_base = data[27]
        self.FP2_emit1 = data[28]
        self.FP2_emit2 = data[29]
        self.FP3_base = data[30]
        self.FP3_emit1 = data[31]
        self.FP3_emit2 = data[32]
        self.custom_prog_param1 = data[33]
        self.custom_prog_param2 = data[34]
        self.custom_prog_param3 = data[35]
        self.custom_prog_status = data[37]
        self.zigzag_target = data[38]
        self.growth_rate = data[39]
        self.error = ""

    def error(self, msg):
        self.error = msg
