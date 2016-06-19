import objectSender
from time import sleep

__receiver = objectSender.objReceiver(("127.0.0.1",5001))
while 1:
    print __receiver.recvfrom()
