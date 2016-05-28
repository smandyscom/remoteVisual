from time import sleep
import pygame

pygame.joystick.init()
axisIndex=0
joystick = pygame.joystick.Joystick(axisIndex)

joystick.init()
print joystick.get_numaxes()
var=1
while var == 1:
  print joystick.get_button(1)
  sleep(0.1)

