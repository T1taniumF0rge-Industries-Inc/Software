'''
 * Keyestudio 24 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 19.2
 * Servo test 2
 * http://www.keyestudio.com
'''
from utime import sleep
from machine import Pin
from machine import PWM

pwm = PWM(Pin(0))#舵机引脚接GP0
pwm.freq(50)#20ms的周期，所以频率为50Hz
'''
角度对应的占空比
0°----2.5%----1638
45°----5%----3276
90°----7.5%----4915
135°----10%----6553
180°----12.5%----8192
考虑到误差，将占空比定在1000~9000，这样可以顺利转动0~180度
'''
# 设置伺服马达的转动角度
def setServoCycle (position):
    pwm.duty_u16(position)
    sleep(0.01)

# 将转动角度换算成占空比
def convert(x, i_m, i_M, o_m, o_M):
    return max(min(o_M, (x - i_m) * (o_M - o_m) // (i_M - i_m) + o_m), o_m)

while True:
    for degree in range(0, 180, 1):#从0°转动到180°
        pos = convert(degree, 0, 180, 1000, 9000)
        setServoCycle(pos)

    for degree in range(180, 0, -1):#从180°转动到0°
        pos = convert(degree, 0, 180, 1000, 9000)
        setServoCycle(pos)
