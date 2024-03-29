from hx711 import HX711
import RPi.GPIO as GPIO
import numpy as np


def take_reading():
    GPIO.setmode(GPIO.BCM)
    hx711 = HX711(
        dout_pin=13,
        pd_sck_pin=6,
        channel='A',
        gain=64
    )

    hx711.reset()  # Before we start, reset the HX711 (not obligate)
    measures = hx711.get_raw_data(times=3)

    return round(np.median(measures))
