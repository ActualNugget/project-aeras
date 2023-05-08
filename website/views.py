from flask import Blueprint, render_template

# from V2.counter import level_pax
# from V2.counter import lift_pax

# Current floor data:


# lift_pax = 4

views = Blueprint('views', __name__)


@views.route('/')
def home():

    return render_template("home.html", lift_pax=counters[lift], level_pax=counters[level])
