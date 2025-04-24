'''
 * Keyestudio 24 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 26
 * button control LED
 * http://www.keyestudio.com
'''
from machine import Pin
import time

button = Pin(16, Pin.IN)
LED = Pin(15, Pin.OUT)
touch = False

def toggle_handle(pin):
    global touch
    touch = not touch

button.irq(trigger = Pin.IRQ_FALLING, handler = toggle_handle)

while True:
    LED.value(touch)
    time.sleep(0.01)