from time import sleep
import pygame
import joystickCommandPack
import objectTransmission

receiver = objectTransmission.objReceiver(('127.0.0.1', 5001))

while 1:
    print receiver.recvfrom()
