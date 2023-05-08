from website import create_app
from V2.counter import counter
from threading import Thread


# The counters
def update_counters():
    global publisher
    counter(publisher)

update_thread = Thread(target=update_counters)
update_thread.start()

# Flask app
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
