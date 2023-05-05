# TODO: count() people in lift now
# TODO: Carpark sensor code
# TODO: Carpark counter code


import RPi.GPIO as GPIO
from led_function import led_function

# GPIO Setup
GPIO.setmode(GPIO.BCM)
display_pins = [17,27,22,10,9,11,5]
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
    count()


try:
    # Lift Up
    GPIO.setup(lift_up_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(lift_up_pin,GPIO.RISING,callback=lift_up, bouncetime=200)

    # Lift Down
    GPIO.setup(lift_down_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(lift_down_pin,GPIO.RISING,callback=lift_down, bouncetime=200)

    # Lift Close
    # GPIO.setup(lift_close_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    # GPIO.add_event_detect(lift_close_pin,GPIO.RISING,callback=lift_close, bouncetime=200)

    message = input("Press enter to quit\n\n") # Run until someone presses enter

finally:
    GPIO.cleanup()
