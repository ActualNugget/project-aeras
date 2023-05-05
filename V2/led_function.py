# Import required libraries
import RPi.GPIO as GPIO

def led_function(numDisplay):

    display_list = [17,27,22,10,9,11,5] # define GPIO ports to use

    # Use BCM GPIO references instead of physical pin numbers
    GPIO.setmode(GPIO.BCM)

    # Set all pins as output
    GPIO.setwarnings(False)
    for pin in display_list:
        GPIO.setup(pin,GPIO.OUT) # setting pins
        GPIO.setup(6,GPIO.OUT) # setting dot pin
        GPIO.setwarnings(True)

    # DIGIT map as array of array
    arrSeg = [[1,1,1,1,1,1,0],\
            [0,1,1,0,0,0,0],\
            [1,1,0,1,1,0,1],\
            [1,1,1,1,0,0,1],\
            [0,1,1,0,0,1,1],\
            [1,0,1,1,0,1,1],\
            [1,0,1,1,1,1,1],\
            [1,1,1,0,0,0,0],\
            [1,1,1,1,1,1,1],\
            [1,1,1,1,0,1,1]]

    GPIO.output(6,0) # DOT pin

    # Display number in argument
    if numDisplay == 10:
        GPIO.cleanup()
    else:
        GPIO.output(display_list, arrSeg[numDisplay])
