# TODO: count() people in lift now
# TODO: Carpark sensor code
# TODO: Carpark counter code


import RPi.GPIO as GPIO
from led_function import led_function
from weight_sensor import take_reading
from weight_analysis import weight_to_people

# GPIO Setup
GPIO.setmode(GPIO.BCM)
display_pins = [17, 27, 22, 10, 9, 11, 5]
dout_pin = 13
pd_sck_pin = 6
lift_up_pin = 15
lift_down_pin = 18
lift_close_pin = 14

level = 1


def lift_up(channel):
    global level
    if level < 5:
        level += 1
        led_function(level)
        print(level)


def lift_down(channel):
    global level
    if level > 1:
        level -= 1
        led_function(level)
        print(level)


def lift_close(channel):
    global level
    readings = take_reading()
    pax = weight_to_people(readings)

try:
    # Lift Up
    GPIO.setup(lift_up_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(lift_up_pin, GPIO.RISING, callback=lift_up, bouncetime=200)

    # Lift Down
    GPIO.setup(lift_down_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(lift_down_pin, GPIO.RISING, callback=lift_down, bouncetime=200)

    # Lift Close
    GPIO.setup(lift_close_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(lift_close_pin,GPIO.RISING,callback=lift_close, bouncetime=200)

    message = input("Press enter to quit")  # Run until someone presses enter

    # Main Loop

        # If lift close, calculate and store the number of people on each floor.

        # Taking a reading from the weight sensor when button3 'closedoor' is pressed

        # Taking in a reading of current floor

        # Calculating the number of people using weight analysis

        # Add number of people in current floor array

finally:
    GPIO.cleanup()
