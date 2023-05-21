import RPi.GPIO as GPIO
import time
import numpy as np
from collections import defaultdict
from led_function import led_function
from weight_sensor import take_reading
from weight_analysis import weight_to_people
from ultrasonic_dist import distance


def counter():
    global level, counters  # Necessary for the button interrupts to work when run in main.py

    try:
        # GPIO Setup
        GPIO.setmode(GPIO.BCM)
        # Display
        display_pins = [17, 27, 22, 10, 9, 11, 5]
        # Weight
        dout_pin = 13
        pd_sck_pin = 6
        # Buttons
        lift_up_pin = 15
        lift_down_pin = 18
        lift_close_pin = 14
        # Ultrasonic
        trigger_pin_1 = 26
        echo_pin_1 = 4
        trigger_pin_2 = 3
        echo_pin_2 = 2
        # Ultrasonic Trigger Distance
        trigger_distance = 8

        # Init counters
        level = 1
        lift_pax = 0
        level_pax = defaultdict(lambda: 0)
        counters = {"lift": lift_pax, "levels": level_pax}
        led_function(level)

        # Lift Up
        def lift_up(channel):
            global level
            if level < 5:
                level += 1
                led_function(level)
                # print(level)
        GPIO.setup(lift_up_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(lift_up_pin, GPIO.RISING,
                              callback=lift_up, bouncetime=500)

        # Lift Down
        def lift_down(channel):
            global level
            if level > 1:
                level -= 1
                led_function(level)
                # print(level)
        GPIO.setup(lift_down_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(lift_down_pin, GPIO.RISING,
                              callback=lift_down, bouncetime=500)

        # Lift Close
        def lift_close(channel):
            global level, counters
            print("before:", counters)
            readings = take_reading()
            lift_pax_new = weight_to_people(readings)
            delta = lift_pax_new - counters["lift"]
            counters["lift"] = lift_pax_new
            counters["levels"][level] = counters["levels"][level] - delta
            if counters["levels"][level] < 0:
                counters["levels"][level] = 0
            # print(lift_pax, "delta: ", delta)
            print(counters)
        GPIO.setup(lift_close_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(lift_close_pin, GPIO.RISING,
                              callback=lift_close, bouncetime=4000)

        # Weirdness:
        # if bouncetime is shorter than callback execute time, callback executes twice

        # set GPIO direction (IN / OUT)
        GPIO.setup(trigger_pin_1, GPIO.OUT)
        GPIO.setup(trigger_pin_2, GPIO.OUT)
        GPIO.setup(echo_pin_1, GPIO.IN)
        GPIO.setup(echo_pin_2, GPIO.IN)
        loop_count = 0

        # The Big Loop
        while True:
            while True:
                # print("loop", loop_count)
                # Carpark Counter
                leave = []
                enter = []
                for i in range(3):
                    try:
                        leave.append(distance(trigger_pin_1, echo_pin_1))
                    except SystemError:
                        leave.append(15)
                    try:
                        enter.append(distance(trigger_pin_2, echo_pin_2))
                    except SystemError:
                        enter.append(15)

                # print(np.median(enter), np.median(exit))

                if np.median(enter) < trigger_distance:
                    counters["levels"][1] += 1
                    if counters["levels"][1] < 0:
                        counters["levels"][1] = 0
                    print("Carpark: +1", "%.1f cm" %
                          np.median(enter), counters["levels"][1])

                    time.sleep(1)
                elif np.median(leave) < trigger_distance:
                    counters["levels"][1] -= 1
                    if counters["levels"][1] < 0:
                        counters["levels"][1] = 0
                    print("Carpark: -1", "%.1f cm" %
                          np.median(leave), counters["levels"][1])
                    time.sleep(1)
                # print(carpark)
                # loop_count += 1
                time.sleep(0.1)
            yield counters
        # message = input("Press enter to quit") # Run until someone presses enter

    finally:
        GPIO.cleanup()


if __name__ == '__main__':
    counter()
