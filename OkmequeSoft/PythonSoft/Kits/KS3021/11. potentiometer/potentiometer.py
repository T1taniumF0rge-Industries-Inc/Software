'''
 * Keyestudio 24 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 11
 * Rotary potentiometer
 * http://www.keyestudio.com
'''
import machine
import utime

potentiometer = machine.ADC(26)

while True:
    pot_value = potentiometer.read_u16()
    print(pot_value,end='\r')
    utime.sleep(0.1)
