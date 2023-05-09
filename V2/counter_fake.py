# import RPi.GPIO as GPIO
import time
from collections import defaultdict
from led_function import led_function
from weight_sensor import take_reading
from weight_analysis import weight_to_people
from ultrasonic_dist import distance

def counter():
    global level, counters # Necessary for the button interrupts to work when run in main.py

    try:

        # The Big Loop
        while True:

            counters = {"lift": 1,
                        "levels": {1: 1,
                                   2: 1,
                                   3: 1,
                                   4: 1,
                                   5: 1}}
            time.sleep(10)

            counters = {"lift": 2,
                        "levels": {1: 2,
                                   2: 2,
                                   3: 2,
                                   4: 2,
                                   5: 2}}
            time.sleep(10)

            counters = {"lift": 3,
                        "levels": {1: 3,
                                   2: 3,
                                   3: 3,
                                   4: 3,
                                   5: 3}}
            time.sleep(10)
    finally:
        print("cleanup!")

if __name__ == '__main__':

    counter()