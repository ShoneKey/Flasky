from flask import Flask, redirect
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


@app.route("/")
def index():
    return redirect('https://baidu.com')


@app.route("/user/<name>")
def user(name):
    return '<h1>Hello, %s!</h1>' % name


if __name__ == '__main__':
    manager.run()
