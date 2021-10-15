from flask import Flask, request
from utils import get_req

app = Flask(__name__)
client = app.test_client()

@app.route('/')
def index():
    return ( '<a href="https://github.com/AbramtsevFV/grav/blob/master/README.md">ReadMe</a>')


@app.route('/grav')
def grav():
    """Главный роут"""
    params = request.args['q']
    result = get_req(params)
    return result


if __name__ == '__main__':
    app.run()
