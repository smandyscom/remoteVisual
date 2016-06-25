from time import sleep
import pygame
import joystickCommandPack
import objectTransmission

receiver = objectTransmission.objReceiver(('', 5001))

while 1:
    print receiver.recvfrom()
