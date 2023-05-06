import numpy as np

# Calculating the number of people from load cell readings

eg_readings = [153930, 152482, 152932]


def weight_to_people(readings):
    readings_avg = round(np.average(readings))
    print(readings_avg)
    pax = 0
    if readings_avg >= 154000:
        pax = 0
    elif readings_avg in range(148000, 154000):
        pax = 1
    elif readings_avg in range(144000, 148000):
        pax = 2
    elif readings_avg in range(140000, 144000):
        pax = 3
    else:
        print('none')

    return pax


# Count the number of people
# Take the reading from weight sensor when button3 is pressed
# store number of people

print(weight_to_people(eg_readings))
