from website import create_app, Publisher
from V2.counter import counter
from threading import Thread

publisher = Publisher()
level = 1

# # The counters
# def update_counters(publisher):
#     counter(publisher)

# update_thread = Thread(target=update_counters(publisher))
# update_thread.start()


# Flask app
app = create_app(publisher)

if __name__ == '__main__':
    app.run(debug=True)