from website import create_app
from counter import counter
from collections import defaultdict
from flask import Flask, Blueprint, render_template
# from multiprocessing import Process

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hhjsjiwueuioqwuro'

# from .views import views
# from .auth import auth

# app.register_blueprint(views, url_prefix='/')
# app.register_blueprint(auth, url_prefix='/')


# Init counters - see inside counter.py
level = 1
lift_pax = 0
level_pax = defaultdict(lambda: 0)
counters = {"lift": lift_pax, "levels": level_pax}


lift_pax = 6
level_pax = {1: 2,
             2: 4,
             3: 4,
             4: 4,
             5: 1}

# views = Blueprint('views', __name__)


# @views.route('/')
# def home():

#     return render_template("home.html", lift_pax=lift_pax, level_pax=level_pax)


@app.route("/")
def home():
    return render_template('home.html', lift_pax=lift_pax, level_pax=level_pax)


gen_total = counter()  # initate the function out of the scope of update route


@app.get("/update")
def update():
    global gen_total  # get the global iterator

    # return the next value in iterator
    return str(next(gen_total))


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
    # flask_proc = Process(target=flask_app, args=(app,))
    # flask_proc.start()

    # counter()
