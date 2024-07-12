from machine import Pin
from time import sleep
A1led = Pin(2, Pin.OUT)
A0led = Pin(0, Pin.OUT)
B1led = Pin(23, Pin.OUT)
B0led = Pin(22, Pin.OUT)

A1button = Pin(32, Pin.IN)
A0button = Pin(33, Pin.IN)
B1button = Pin(26, Pin.IN)
B0button = Pin(27, Pin.IN)

while True:
    if A1button.value():
        A1led.value(True)
        B0led.value(True)
        sleep(1)
        A1led.value(False)
        B0led.value(False)
        sleep(1)
        
    elif A0button.value():
        A0led.value(True)
        B1led.value(True)
        sleep(1)
        A0led.value(False)
        B1led.value(False)
        sleep(1)
        
    elif B1button.value():
        A1led.value(True)
        A0led.value(True)
        B1led.value(True)
        B0led.value(True)
        sleep(1)
        A1led.value(False)
        A0led.value(False)
        B1led.value(False)
        B0led.value(False)
        sleep(1)
        
    elif B0button.value():
        A1led.value(True)
        sleep(0.5)
        A1led.value(False)
        sleep(0.5)
        A0led.value(True)
        sleep(0.5)
        A0led.value(False)
        sleep(0.5)
        B1led.value(True)
        sleep(0.5)
        B1led.value(False)
        sleep(0.5)
        B0led.value(True)
        sleep(0.5)
        B0led.value(False)
        sleep(0.5)
        
