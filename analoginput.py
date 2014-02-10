#!/usr/bin/python

from Adafruit_BBIO import ADC, PWM
from math import sin, pi
import time

ADC.setup()
PWM.start("P8_13", 0)

while True:
    lectura = ADC.read("P9_39")
    PWM.set_duty_cycle("P8_13", lectura)
