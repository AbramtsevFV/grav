import json
import utils
from app import client



def test_request(result):
    assert utils.get_req('k.bx@ya.ru') == result[0]


def test_bad_request():
    assert utils.get_req('k@ya.ru') == {'message': 'The user with the email k@ya.ru  was not found'}


def test_API(result, email):
    for i, n in enumerate(result):
        res = client.get(f'/grav?q={email[i]}')
        assert res.status_code == 200
        assert json.loads(res.data) == n
