import socket
import StringIO
import pickle

# reflect whole joystick input infoj
class commandPack:
    axisValues = [0.0, 0.0]
    buttonValues = [0, 0]
    def __init__(self):
        self.axisValues = [0.0, 0.0]
        self.buttonValues = [0, 0]
    def __str__(self):
        return "%s;%s" % (self.axisValues, self.buttonValues)

class objSender:
    def __init__(self, remoteAddress):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.remoteAddress = remoteAddress
        self.stream = StringIO.StringIO()

    def sendto(self, objGoingToSend):
        #rewind stream
        self.stream.seek(0)
        pickle.dump(objGoingToSend, self.stream)
        self.socket.sendto(self.stream.getvalue(), self.remoteAddress)

class objReceiver:
    def __init__(self, localAddress):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(localAddress)
    def recvfrom(self):
        buf, remoteAddress = self.socket.recvfrom(1024)
        return pickle.load(StringIO.StringIO(buf))

