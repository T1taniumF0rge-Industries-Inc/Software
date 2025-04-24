'''
 * Keyestudio 24 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 9
 * Passive buzzer
 * http://www.keyestudio.com
'''
from machine import Pin, PWM
from time import sleep
buzzer = PWM(Pin(0))

buzzer.duty_u16(1000)
def demo():
    buzzer.freq(523)#DO
    sleep(0.5)
    buzzer.freq(586)#RE
    sleep(0.5)
    buzzer.freq(658)#MI
    sleep(0.5)
    buzzer.freq(697)#FA
    sleep(0.5)
    buzzer.freq(783)#SO
    sleep(0.5)
    buzzer.freq(879)#LA
    sleep(0.5)
    buzzer.freq(987)#SI
    sleep(0.5)
    buzzer.duty_u16(0)
def test():
    buzzer.freq(8)
    sleep(0.5)
    buzzer.duty_u16(0)
test()