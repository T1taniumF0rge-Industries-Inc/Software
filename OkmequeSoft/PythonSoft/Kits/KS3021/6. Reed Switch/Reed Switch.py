'''
 * Keyestudio 24 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 6
 * Reed Switch
 * http://www.keyestudio.com
'''
from machine import Pin
import time

ReedSensor = Pin(18, Pin.IN)
while True:
    value = ReedSensor.value()
    print(value, end = " ")
    if value == 0:
        print("A magnetic field")
    else:
        print("There is no magnetic field")
    time.sleep(0.1)