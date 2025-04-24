'''
 * Keyestudio 24 in 1 Starter Kit for Raspberry Pi Pico
 * lesson 29
 * play music
 * http://www.keyestudio.com
'''
from machine import Pin, PWM
from utime import sleep
buzzer = PWM(Pin(15))

tones = {
"D1": 262,
"D2": 293,
"D3": 329,
"D4": 349,
"D5": 392,
"D6": 440,
"D7": 494,
"M1": 523,
"M2": 586,
"M3": 658,
"M4": 697,
"M5": 783,
"M6": 879,
"M7": 987,
"H1": 1045,
"H2": 1171,
"H3": 1316,
"H4": 1393,
"H5": 1563,
"H6": 1755,
"H7": 1971
}

song = ["D5","D5","D6","D5","M1","D7",
        "D5","D5","D6","D5","M2","M1",
        "D5","D5","M5","M3","M1","D7","D6",
        "M4","M4","M3","M1","M2","M1"
]

durt = [0.25, 0.25, 0.5, 0.5, 0.5, 1,
       0.25, 0.25, 0.5, 0.5, 0.5, 1,
       0.25, 0.25, 0.5, 0.5, 0.5, 0.5, 0.5,
       0.25, 0.25, 0.5, 0.5, 0.5, 1
]

def playtone(frequency):
    buzzer.duty_u16(1000)
    buzzer.freq(frequency)

def bequiet():
    buzzer.duty_u16(0)

def playsong(mysong):
    for i in range(len(mysong)):
        playtone(tones[mysong[i]])
        sleep(durt[i])
    bequiet()
playsong(song)
