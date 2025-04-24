'''
 * Keyestudio 24 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 20
 * Ultrasonic
 * http://www.keyestudio.com
'''
from machine import Pin
import utime

# 超声波测距，单位：厘米
def getDistance(trigger, echo):
    # 产生10us的方波
    trigger.low()   #预先给出一个短的低电平，以确保一个干净的高脉冲:
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(10)#拉高电平後，等待10微秒后，立即设置为低电平
    trigger.low()
    
    while echo.value() == 0: #建立一个while循环检测回波引腳是否值為0，记录当时时间
        start = utime.ticks_us()
    while echo.value() == 1: #建立一个while循环检测回波引腳是否值為1，记录当时时间
        end = utime.ticks_us()
    d = (end - start) * 0.0343 / 2 #声波行進時間 x 声速(343.2 m/s，即每微秒0.0343公分)，來回距離再除以2
    return d

# 设置引脚
trigger = Pin(14, Pin.OUT)
echo = Pin(13, Pin.IN)
# 主程序
while True:
    distance = getDistance(trigger, echo)
    print("The distance is ：{:.2f} cm".format(distance))
    utime.sleep(0.1)
