#!/usr/bin/python

from Adafruit_BBIO import PWM
from math import sin, pi
import time

def sinewave(resolution):
    i = 0
    while i < resolution + 1:
        yield sin(pi*i/resolution)
        if i == resolution:
            i = 0
        else:
            i += 1

PWM.start("P8_13", 100)
seno = sinewave(100)

while True:
    PWM.set_duty_cycle("P8_13", 100.0*(1.0 - seno.next()))
    time.sleep(1.0/100.0)
