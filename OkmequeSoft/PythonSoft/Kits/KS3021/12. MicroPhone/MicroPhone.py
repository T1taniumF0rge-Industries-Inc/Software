'''
 * Keyestudio 24 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 12
 * MicroPhone
 * http://www.keyestudio.com
'''
import machine
import utime

MicroPhone = machine.ADC(27)
while True:
    value = MicroPhone.read_u16()
    print(value)
    utime.sleep(0.1)