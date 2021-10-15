import json

import pytest

import utils
from app import client


def test_request(result):
    assert utils.get_req('k.bx@ya.ru') == result[0]


def test_bad_request():
    assert utils.get_req('k@ya.ru') == {'message': 'The user with the email k@ya.ru  was not found'}


@pytest.mark.parametrize('a', [0, 1, 2, 3, 4, 5, 6, 7])
def test_API(result, email, a):
    res = client.get(f'/grav?q={email[a]}')
    assert res.status_code == 200
    assert json.loads(res.data) == result[a]
