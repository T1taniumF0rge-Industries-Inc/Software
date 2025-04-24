'''
 * Keyestudio 24 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 15
 * Film pressure sensor
 * http://www.keyestudio.com
'''
import machine
import utime

film = machine.ADC(1)
while True:
    value = film.read_u16()
    print(value)
    utime.sleep(0.1)
