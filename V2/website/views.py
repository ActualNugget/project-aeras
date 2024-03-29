from flask import Blueprint, render_template

# from V2.counter import level_pax
# from V2.counter import lift_pax

# Current floor data:


lift_pax = 6
level_pax = {1: 2,
             2: 4,
             3: 4,
             4: 4,
             5: 1}

views = Blueprint('views', __name__)


@views.route('/')
def home():

    return render_template("home.html", lift_pax=lift_pax, level_pax=level_pax)


@views.get("/update")
def update():
    global gen_total  # get the global iterator

    # return the next value in iterator
    return str(next(gen_total))
