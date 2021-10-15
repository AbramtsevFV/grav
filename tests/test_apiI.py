import json

import pytest

import utils
from app import client


def test_request(result):
    assert utils.get_req('k.bx@ya.ru') == result[0]


def test_bad_request():
    assert utils.get_req('k@ya.ru') == {'message': 'The user with the email k@ya.ru  was not found'}


@pytest.mark.parametrize('a, email',
                         [
                             (0, 'k.bx@ya.ru'),
                             (1, 'eehzntm5@hotmail.com'),
                             (2, 'manuruel@yahoo.com'),
                             (3, 'russellebb912@hotmail.com'),
                             (4, 'jnkitchener@btinternet.com'),
                             (5, 'ras-nie@web.de'),
                             (6, 'ghagen4@gmail.com'),
                             (7, 'mattdhoey@gmail.com')
                         ]
                         )
def test_API(result, a, email):
    res = client.get(f'/grav?q={email}')
    assert res.status_code == 200
    assert json.loads(res.data) == result[a]
