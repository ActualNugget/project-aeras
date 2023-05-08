from website import create_app
from counter import counter
from collections import defaultdict
from multiprocessing import Process
import RPi.GPIO as GPIO

def flask_app(app):
    app.run(debug=True)


app = create_app()
# Init counters
level = 1
lift_pax = 0
level_pax = defaultdict(lambda: 0)
counters = {"lift": lift_pax, "levels": level_pax}

if __name__ == '__main__':
    try:
        flask_proc = Process(target=flask_app, args=(app, ))
        flask_proc.start()

        count_proc = Process(target=counter)
        count_proc.start()
    finally:
        GPIO.cleanup()
