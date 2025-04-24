'''
 * Keyestudio 24 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 1.2
 * Blink
 * http://www.keyestudio.com
'''
from machine import Pin
import time

led = Pin(0, Pin.OUT)# 构建led对象,外接LED灯连接与引脚0相连，并设置引脚0为输出模式
while True:
    led.value(1)# led点亮
    time.sleep(1)# 等待1秒
    led.value(0)# led熄灭
    time.sleep(1)# 等待1秒