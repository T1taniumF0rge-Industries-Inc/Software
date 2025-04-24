'''
 * Keyestudio 24 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 3
 * button
 * http://www.keyestudio.com
'''
from machine import Pin
import time

button = Pin(1, Pin.IN, Pin.PULL_UP)

while True:
    if button.value() == 0:
        print("\rYou pressed the button!",end='\r')   #按下则打印相应信息
    else:
        print("\rYou loosen the button!",end='\r')
    time.sleep(0.1) #延时0.1秒
