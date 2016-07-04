from time import sleep
import pigpio
import pygame
import joystickCommandPack
import objectTransmission
import buttonIncrementor
receiver = objectTransmission.objReceiver(('', 5001))
piController = pigpio.pi()
__buttonIncrementor = buttonIncrementor.buttonIncrementor()
while 1:
    # print receiver.recvfrom()
    pack = receiver.recvfrom()
    # piController.set_servo_pulsewidth(21, (pack.axisValues[0]+1) * 750 + 750)
    # piController.set_PWM_dutycycle(18, (pack.axisValues[3]+1) * 125)
    # piController.set_servo_pulsewidth(18, pack.axis2Servo()[0])
    # piController.set_servo_pulsewidth(21, pack.axis2Servo()[1])
    piController.hardware_PWM(19, 100,  pack.axis2Pwm()[2])
    if pack.buttonValues[0] == 1:
        __buttonIncrementor.move(True)
    if pack.buttonValues[1] == 1:
        __buttonIncrementor.move(False)
    piController.set_servo_pulsewidth(21, __buttonIncrementor.currentPosition)
    print pack
