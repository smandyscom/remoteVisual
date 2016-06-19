import objectSender
from time import sleep

__sender = objectSender.objSender(("127.0.0.1",5001))
while 1:
    __sender.sendto(objectSender.commandPack())
    sleep(1)
