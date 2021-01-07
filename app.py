import os

from flask import Flask

app = Flask(__name__)


@app.route('/user/<username>')
def user(username=None):
    string = 'Current user: ' + str(username)
    p = 'data'
    if not os.path.exists(p):
        os.mkdir(p)

    with open(f'{p}/{username}.txt', 'xt') as f:
        f.write(string)

    return 'Current user: ' + str(username)


@app.route('/health')
def health():
    return 'Your health matters!'


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8084)
