import json

import pytest


@pytest.fixture(scope='function')
def result():
    with open("tests/result.json", 'r') as f_o:
        valid_json_answer = json.load(f_o)

    return valid_json_answer


@pytest.fixture(scope='function')
def email():
    email = ['k.bx@ya.ru', 'eehzntm5@hotmail.com', 'manuruel@yahoo.com', 'russellebb912@hotmail.com',
             'jnkitchener@btinternet.com', 'ras-nie@web.de', 'ghagen4@gmail.com', 'mattdhoey@gmail.com']
    return email
