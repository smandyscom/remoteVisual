from time import sleep
import pigpio
import pygame
import joystickCommandPack
import objectTransmission

receiver = objectTransmission.objReceiver(('', 5001))
piController = pigpio.pi()
while 1:
    # print receiver.recvfrom()
    pack = receiver.recvfrom()
    piController.set_servo_pulsewidth(21, (pack.axisValues[0]+1) * 750 + 750)
    piController.set_PWM_dutycycle(18, (pack.axisValues[3]+1) * 125)
    print pack
