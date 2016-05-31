from time import sleep
import pygame
#in order to drive event.get , need to initialize base module
pygame.init()
pygame.joystick.init()
axisIndex=0
joystick = pygame.joystick.Joystick(axisIndex)

joystick.init()
print ("Joystick initialize status {0}".format(joystick.get_init()))
print ("Joystick name {0}".format(joystick.get_name()))
var=1
while var == 1:
   pygame.event.get()
   print ("Axis value {:>6.3f}".format(joystick.get_axis(0)))
   sleep(0.1)

