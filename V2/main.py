from website import create_app
from multiprocessing import Process

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
