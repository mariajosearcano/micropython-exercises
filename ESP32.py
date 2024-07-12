from machine import Pin
from time import sleep
A1led = Pin(17, Pin.OUT)
A0led = Pin(16, Pin.OUT)
B1led = Pin(2, Pin.OUT)
B0led = Pin(0, Pin.OUT)
while True:
    A1led.value(not A1led.value())
    sleep (1)
    A1led.value(not A1led.value())
    sleep (1)
    
    A0led.value(not A0led.value())
    sleep (0.25)
    A0led.value(not A0led.value())
    sleep (0.25)
    
    B1led.value(not B1led.value())
    sleep (0.125)
    B1led.value(not B1led.value())
    sleep (0.125)
    
    B0led.value(not B0led.value())
    sleep (0.0625)
    B0led.value(not B0led.value())
    sleep (0.0625)