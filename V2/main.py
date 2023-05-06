# TODO: count() people in lift now
# TODO: Carpark sensor code
# TODO: Carpark counter code


import RPi.GPIO as GPIO
from led_function import led_function

# GPIO Setup
GPIO.setmode(GPIO.BCM)
# Display
display_pins = [17,27,22,10,9,11,5]
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

try:
    # Lift Up
    def lift_up(channel):
        global level
        if level < 5:
            level += 1
            led_function(level)
            print(level)
    GPIO.setup(lift_up_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(lift_up_pin, GPIO.RISING, callback=lift_up, bouncetime=200)

    # Lift Down
    def lift_down(channel):
        global level
        if level > 1:
            level -= 1
            led_function(level)
            print(level)
    GPIO.setup(lift_down_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(lift_down_pin, GPIO.RISING, callback=lift_down, bouncetime=200)

    # Lift Close
    def lift_close(channel):
        global level
        count()
    # GPIO.setup(lift_close_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    # GPIO.add_event_detect(lift_close_pin,GPIO.RISING,callback=lift_close, bouncetime=200)

    #set GPIO direction (IN / OUT)
    GPIO.setup(trigger_pin_1, GPIO.OUT)
    GPIO.setup(trigger_pin_2, GPIO.OUT)
    GPIO.setup(echo_pin_1, GPIO.IN)
    GPIO.setup(echo_pin_2, GPIO.IN)

    message = input("Press enter to quit") # Run until someone presses enter

finally:
    GPIO.cleanup()
