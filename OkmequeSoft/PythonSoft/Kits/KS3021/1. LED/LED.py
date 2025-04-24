'''
 * Keyestudio 24 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 1.1
 * turn on led
 * http://www.keyestudio.com
'''
from machine import Pin

led = Pin(0, Pin.OUT)# 构建led对象,外接LED灯连接与引脚0相连，并设置引脚0为输出模式

led.value(1)# 高电平点亮
    