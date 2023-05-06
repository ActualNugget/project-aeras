#long and short distances -> triggers the counter 
import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
trigger_pin_1 = 26
echo_pin_1 = 4
trigger_pin_2 = 3
echo_pin_2 = 2

 
#set GPIO direction (IN / OUT)
GPIO.setup(trigger_pin_1, GPIO.OUT)
GPIO.setup(trigger_pin_2, GPIO.OUT)
GPIO.setup(echo_pin_1, GPIO.IN)
GPIO.setup(echo_pin_2, GPIO.IN)

def distance(GPIO_TRIGGER, GPIO_ECHO):
    # Reset Trigger
    # print("sleepin")
    # GPIO.output(GPIO_TRIGGER, 0)
    # time.sleep(2)
    # GPIO.output(GPIO_TRIGGER, 1)

    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime

    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
# try:
#     count = 0
#     while True:
#         exit = distance(trigger_pin_1, echo_pin_1)
#         entry = distance(trigger_pin_2, echo_pin_2)
#         # print ("Entry = %.1f cm" % entry)
#         # print ("Exit = %.1f cm" % exit)

#         if entry < 7:
#             count += 1
#             time.sleep(1)
#         elif exit < 7:
#             count -= 1
#             time.sleep(1)
#         print(count)

#         time.sleep(0.1)

#     # Reset by pressing CTRL + C
# except KeyboardInterrupt:
#     print("Measurement stopped by User")
#     GPIO.cleanup()