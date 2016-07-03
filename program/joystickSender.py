from time import sleep
import os
import pygame
import joystickCommandPack
import objectTransmission

pygame.init()
pygame.joystick.init()

js = pygame.joystick.Joystick(0)
js.init()
commandPack = joystickCommandPack.commandPack()
sender = objectTransmission.objSender(('192.168.10.15', 5001))
while 1:
    # Process all event
    for event in pygame.event.get():
        print event.type
    commandPack.axisValues = [js.get_axis(x) for x in range(js.get_numaxes())]
    commandPack.buttonValues = [js.get_button(x) for x in range(js.get_numbuttons())]
    sender.sendto(commandPack)
    sleep(0.2)
    # os.system("clear")
    print commandPack

