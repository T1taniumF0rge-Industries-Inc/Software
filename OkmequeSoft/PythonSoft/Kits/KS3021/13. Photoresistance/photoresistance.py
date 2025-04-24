'''
 * Keyestudio 24 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 13
 * Photoresistance
 * http://www.keyestudio.com
'''
import machine
import utime

photoresistance = machine.ADC(28)
while True:
    value = photoresistance.read_u16()
    print(value)
    utime.sleep(0.1)

