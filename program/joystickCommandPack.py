class commandPack:
    def __init__(self):
        self.axisValues = [0.0, 0.0]
        self.buttonValues = [0, 0]
    def __str__(self):
        return "%s;%s" % (self.axisValues, self.buttonValues)
    def axis2Servo(self):
        return [(value + 2) * 750 for value in self.axisValues]
    def axis2Pwm(self):
        return [abs(value) * 1000000 for value in self.axisValues]

