'''
 * Keyestudio 24 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 2
 * Traffic_Light
 * http://www.keyestudio.com
'''
import machine
import time

led_red = machine.Pin(14, machine.Pin.OUT)
led_amber = machine.Pin(13, machine.Pin.OUT)
led_green = machine.Pin(12, machine.Pin.OUT)

while True:
    led_green.value(1) # 绿灯亮5秒
    time.sleep(5)# 5秒后
    led_green.value(0)# 绿灯熄灭
    for i in range(3):#黄灯闪烁3次
        led_amber.value(1)
        time.sleep(0.5)
        led_amber.value(0)
        time.sleep(0.5)
    led_red.value(1) # 红灯亮5秒
    time.sleep(5)
    led_red.value(0)
