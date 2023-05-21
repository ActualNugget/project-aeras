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
            counters = {
                "lift": x,
                "levels": {
                    1: random.randint(1, 3),
                    2: random.randint(1, 3), 
                    3: random.randint(1, 3), 
                    4: random.randint(1, 3), 
                    5: random.randint(1, 3),
                },
                "airflow": {
                    "total": 80,
                    1: 0,
                    2: 0,
                    3: 0,
                    4: 0,
                    5: 0,
                    "outdoor": 80,
                },
                }
                # Set the airflow values based on the levels
            for level, value in counters["levels"].items():
                if level in [1, 2, 3, 4, 5]:
                    if value == 1:
                        counters["airflow"][level] = 20
                    elif value == 2:
                        counters["airflow"][level] = 60
                    elif value == 3:
                        counters["airflow"][level] = 80

            yield counters

    finally:
        print("cleanup!")


if __name__ == '__main__':

    counter_fake()
