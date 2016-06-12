from time import sleep
import pygame
from socket import *
import struct
# import socket
# socket part
HOST = "127.0.0.1"
PORT = 5001
sender = socket(AF_INET, SOCK_DGRAM)
# sender.bind((HOST,PORT))
sender.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sender.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

# in order to drive event.get , need to initialize base module
pygame.init()
pygame.joystick.init()
axisIndex = 0
joystick = pygame.joystick.Joystick(axisIndex)

joystick.init()
print ("Joystick initialize status {0}".format(joystick.get_init()))
print ("Joystick name {0}".format(joystick.get_name()))

var = 1
while var == 1:
    pygame.event.get()
    print ("Axis value {:>6.3f}".format(joystick.get_axis(0)))
    sender.sendto(struct.pack("f", joystick.get_axis(0)), (HOST, PORT))
    sleep(0.5)
