from flask import Flask, request
from utils import get_req

app = Flask(__name__)


@app.route('/grav')
def grav():
    """Главный роут"""
    params = request.args['q']
    result = get_req(params)
    return result


if __name__ == '__main__':
    app.run(debug=False)
