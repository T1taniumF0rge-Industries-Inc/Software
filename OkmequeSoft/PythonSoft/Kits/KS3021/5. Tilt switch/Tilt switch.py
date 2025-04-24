'''
 * Keyestudio 24 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 5
 * Tilt switch
 * http://www.keyestudio.com
'''
from machine import Pin
import time

TiltSensor = Pin(17, Pin.IN)

while True:
    value = TiltSensor.value()
    print(value, end = " ")
    if  value== 0:
        print("The switch is turned on")
    else:
        print("The switch is turned off")
    time.sleep(0.1)