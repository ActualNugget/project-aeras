import RPi.GPIO as GPIO
import time
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

        # The Big Loop
        while True:

            # Carpark Counter
            exit = distance(trigger_pin_1, echo_pin_1)
            entry = distance(trigger_pin_2, echo_pin_2)
            # print ("Entry = %.1f cm" % entry)
            # print ("Exit = %.1f cm" % exit)

            if entry < 7:
                counters["levels"][1] += 1
                print("Carpark: +1", "%.1f cm" % entry, counters["levels"][1])
                if counters["levels"][1] < 0:
                    counters["levels"][1] = 0
                time.sleep(1)
            elif exit < 7:
                counters["levels"][1] -= 1
                print("Carpark: -1", "%.1f cm" % exit, counters["levels"][1])
                if counters["levels"][1] < 0:
                    counters["levels"][1] = 0
                time.sleep(1)
            # print(carpark)
            time.sleep(0.1)
        # message = input("Press enter to quit") # Run until someone presses enter

    finally:
        GPIO.cleanup()


if __name__ == '__main__':
    counter()
