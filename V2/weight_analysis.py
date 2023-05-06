import numpy as np


# Calculating the number of people from load cell readings
def weight_to_people(readings):
    print(readings)
    pax = 0
    if readings >= 154000:
        pax = 0
    elif readings in range(148000, 154000):
        pax = 1
    elif readings in range(144000, 148000):
        pax = 2
    elif readings in range(140000, 144000):
        pax = 3
    else:
        print('none')

    return pax
