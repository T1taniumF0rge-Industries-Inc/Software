'''
 * Keyestudio 24 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 30
 * Encoder control RGB
 * http://www.keyestudio.com
'''
import time
from rotary_irq_rp2 import RotaryIRQ
from machine import Pin, PWM

pwm_r = PWM(Pin(9))
pwm_g = PWM(Pin(10))
pwm_b = PWM(Pin(11))

pwm_r.freq(1000)
pwm_g.freq(1000)
pwm_b.freq(1000)

def light(red, green, blue):
    pwm_r.duty_u16(red)
    pwm_g.duty_u16(green)
    pwm_b.duty_u16(blue)

SW=Pin(20,Pin.IN,Pin.PULL_UP)
r = RotaryIRQ(pin_num_clk=18,
              pin_num_dt=19,
              min_val=0,
              reverse=False,
              range_mode=RotaryIRQ.RANGE_UNBOUNDED)

while True:
    val = r.value()
    print(val%3)
    if val%3 == 0:
        light(65535, 0, 0)
    elif val%3 == 1:
        light(0, 65535, 0)
    elif val%3 == 2:
        light(0, 0, 65535)
    time.sleep(0.1)
    
