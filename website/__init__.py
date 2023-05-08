from flask import Flask

class Publisher:
    def __init__(self):
        self.subscribers = set()

    def register(self, subscriber):
        self.subscribers.add(subscriber)
    
    def notify(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)

class Subscriber:
    def __init__(self, app, variable_name) -> None:
        self.app = app
        self.variable_name = variable_name
    
    def update(self, message):
        setattr(self.app, self.variable_name, message)


def create_app(publisher):
    app = Flask(__name__)
    # publisher = Publisher()
    subscriber = Subscriber(app, 'counters')
    publisher.register(subscriber)

    app.config['SECRET_KEY'] = 'hhjsjiwueuioqwuro'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

