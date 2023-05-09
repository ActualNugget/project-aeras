from website import create_app
from counter import counter
from collections import defaultdict
# from multiprocessing import Process


def flask_app(app):
    app.run(debug=True, use_reloader=False)


app = create_app()
# Init counters - see inside counter.py
level = 1
lift_pax = 0
level_pax = defaultdict(lambda: 0)
counters = {"lift": lift_pax, "levels": level_pax}

gen_total = counter()  # initate the function out of the scope of update route


# @app.get("/update")
# def update():
#     global gen_total  # get the global iterator

#     # return the next value in iterator
#     return str(next(gen_total))


if __name__ == '__main__':
    flask_app(app)
    # flask_proc = Process(target=flask_app, args=(app,))
    # flask_proc.start()

    # counter()
