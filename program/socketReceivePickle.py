import socket
import StringIO
import pickle
from time import sleep

class objectGoingToSend:
    field1 = 1
    field2 = 5.8
    def __str__(self):
        return "%s,%s" % (self.field1, self.field2)


receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiver.bind(("127.0.0.1",5001))
while 1:
    # __inter = StringIO.StringIO()
    # pickle.dump(objectGoingToSend(), __inter)
    buf , address = receiver.recvfrom(1024)
    obj = pickle.load(StringIO.StringIO(buf))
    print obj
    sleep(1)
