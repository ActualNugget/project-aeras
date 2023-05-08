from flask import Blueprint, render_template

# from V2.counter import level_pax
# from V2.counter import lift_pax

# Current floor data:


lift_pax = 5
level_pax = {1: 2,
             2: 4,
             3: 4,
             4: 0,
             5: 1}

views = Blueprint('views', __name__)


@views.route('/')
def home():
    
    return render_template("home.html", lift_pax=lift_pax, level_pax=level_pax)
