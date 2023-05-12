# import RPi.GPIO as GPIO
import time
import random
from collections import defaultdict
# from led_function import led_function
# from weight_sensor import take_reading
# from weight_analysis import weight_to_people
# from ultrasonic_dist import distance


def counter_fake():
    global level, counters  # Necessary for the button interrupts to work when run in main.py

    try:

        # The Big Loop
        while True:
            x = random.randint(1, 3)
            counters = {"lift": x, "levels": {1: x, 2: x, 3: x, 4: x, 5: x}}

            yield counters

    finally:
        print("cleanup!")


if __name__ == '__main__':

    counter_fake()
