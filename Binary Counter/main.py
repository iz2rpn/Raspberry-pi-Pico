import machine
import utime
from machine import Pin, PWM
from time import sleep

led15 = machine.Pin(15,machine.Pin.OUT)
led14 = machine.Pin(14,machine.Pin.OUT)
led13 = machine.Pin(13,machine.Pin.OUT)
led12 = machine.Pin(12,machine.Pin.OUT)
led11 = machine.Pin(11,machine.Pin.OUT)
led10 = machine.Pin(10,machine.Pin.OUT)
led9 = machine.Pin(9,machine.Pin.OUT)
led8 = machine.Pin(8,machine.Pin.OUT)
led7 = machine.Pin(7,machine.Pin.OUT)
led6 = machine.Pin(6,machine.Pin.OUT)
led5 = machine.Pin(5,machine.Pin.OUT)
led4 = machine.Pin(4,machine.Pin.OUT)

led = [led4,led5,led6,led7,led8,led9,led10,led11,led12,led13,led14,led15]

speed = 300

buzzerPIN=16
BuzzerObj=PWM(Pin(buzzerPIN))

def buzzer(buzzerPinObject,frequency,sound_duration,silence_duration):
    # Set duty cycle to a positive value to emit sound from buzzer
    buzzerPinObject.duty_u16(int(65536*0.2))
    # Set frequency
    buzzerPinObject.freq(frequency)
    # wait for sound duration
    sleep(sound_duration)
    # Set duty cycle to zero to stop sound
    buzzerPinObject.duty_u16(int(65536*0))
    # Wait for sound interrumption, if needed 
    sleep(silence_duration)

def up():
    buzzer(BuzzerObj,987,0.5,0.1)
    for i in range(0,len(led)):
        led[i].value(1)
        utime.sleep_ms(speed)
        led[i].value(0)
        utime.sleep_ms(speed)
        if len(led) == 15:
            led15.value(0)
            led14.value(0)
            led13.value(0)
            led12.value(0)
            led11.value(0)
            led10.value(0)
            led9.value(0)
            led8.value(0)
            led7.value(0)
            led6.value(0)
            led5.value(0)
            led4.value(0)
        
def down():
    buzzer(BuzzerObj,987,0.5,0.1)
    for i in reversed(range(len(led))):
        led[i].value(1)
        utime.sleep_ms(speed)
        led[i].value(0)
        utime.sleep_ms(speed)
        if len(led) == 0:
            led15.value(0)
            led14.value(0)
            led13.value(0)
            led12.value(0)
            led11.value(0)
            led10.value(0)
            led9.value(0)
            led8.value(0)
            led7.value(0)
            led6.value(0)
            led5.value(0)
            led4.value(0)
        
def binary():
    buzzer(BuzzerObj,987,0.5,0.1)
    for i in range(0,4096):
        for j in range(0,len(led)):
            if i & (1<<j):
                led[j].value(1)  
            else:
                led[j].value(0)
        utime.sleep_ms(speed)
        if len(led) == 15:
            led15.value(0)
            led14.value(0)
            led13.value(0)
            led12.value(0)
            led11.value(0)
            led10.value(0)
            led9.value(0)
            led8.value(0)
            led7.value(0)
            led6.value(0)
            led5.value(0)
            led4.value(0)


while True:
    down()
    up()
    binary()