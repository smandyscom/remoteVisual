import random
import socket
import StringIO
import pickle
from time import sleep
class objectGoingToSend:
    field1 = 1
    field2 = 5.8


sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
__inter = StringIO.StringIO()
while 1:
    # __inter = StringIO.StringIO()
    __inter.seek(0) #rewind file to zero
    obj = objectGoingToSend()
    obj.field2 = random.random()
    pickle.dump(obj, __inter)
    sender.sendto(__inter.getvalue(), ("127.0.0.1", 5001))
    print __inter
    sleep(1)
