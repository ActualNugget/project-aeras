from flask import Blueprint, render_template

# from V2.counter import level_pax
# from V2.counter import lift_pax

# Current floor data:


lift_pax = 9
level_pax = {1: 2,
             2: 2,
             3: 4,
             4: 4,
             5: 6}
counters = {"lift": lift_pax, "levels": level_pax}

views = Blueprint('views', __name__)


@views.route('/')
def home():
    global counters
    return render_template("home.html", lift_pax=counters["lift"], level_pax=counters["levels"])
