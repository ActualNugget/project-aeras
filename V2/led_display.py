# Import required libraries
import sys
import RPi.GPIO as GPIO

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

# Check main arguments errors
if len(sys.argv) > 2:
 print("ERROR: too many arguments")
 sys.exit()
elif len(sys.argv) == 1:
 print("ERROR: missing argument")
 sys.exit()
elif int(sys.argv[1].replace(".", "")) > 10 or int(sys.argv[1].replace(".", ""))<0:
 print("ERROR: insert a number between 0 and 10")
 sys.exit()

# Manage DOT activation
if sys.argv[1].count(".") == 1:GPIO.output(6,1)

# Activate number on display with a value cleaned from final dot
numDisplay = int(sys.argv[1].replace(".", ""))

# Display number in argument
if numDisplay == 10:
 GPIO.cleanup()
else:
 GPIO.output(display_list, arrSeg[numDisplay])

sys.exit()