class commandPack:
    axisValues = [0.0, 0.0]
    buttonValues = [0, 0]
    def __init__(self):
        self.axisValues = [0.0, 0.0]
        self.buttonValues = [0, 0]
    def __str__(self):
        return "%s;%s" % (self.axisValues, self.buttonValues)
    def toServoCommand(self):
        return [(value + 2) * 750 for value in self.axisValues]

