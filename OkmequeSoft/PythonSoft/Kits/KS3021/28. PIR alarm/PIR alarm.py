'''
 * Keyestudio 24 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 28
 * PIR alarm
 * http://www.keyestudio.com
'''
import machine
import utime

sensor_pir = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(25, machine.Pin.OUT)
buzzer = machine.Pin(16, machine.Pin.OUT)

def pir_handler(pin):
    utime.sleep_ms(100)
    if pin.value():
        print("Warning! Intrusion detected！")
        buzzer.value(1)
        for i in range(20):
            led.toggle()
            utime.sleep_ms(100)

sensor_pir.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)

while True:
    led.toggle()
    buzzer.value(0)
    utime.sleep(2)
