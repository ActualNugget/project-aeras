from website import create_app, Publisher
from V2.counter import counter
from threading import Thread
from collections import defaultdict

publisher = Publisher()

# Init counters
level = 1
lift_pax = 0
level_pax = defaultdict(lambda: 0)
counters = {"lift": lift_pax, "levels": level_pax}

# Update counters
def update_counters(publisher):
    counter(publisher)

update_thread = Thread(target=update_counters, args=(publisher, ))
update_thread.start()


# Flask app
app = create_app(publisher)

if __name__ == '__main__':
    app.run(debug=True)