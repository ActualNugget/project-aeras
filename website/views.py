from flask import Blueprint, render_template
# from V2.main import level_pax
# from V2.main import lift_pax

# Current floor data:
level_pax = {
    1:3,
    2:4,
    3:5,
    4:1,
    5:4
    }

lift_pax = 4

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html", lift_pax=lift_pax, level_pax=level_pax)
