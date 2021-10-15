import json

import pytest


@pytest.fixture
def result():
    with open("tests/result.json", 'r') as f_o:
        valid_json_answer = json.load(f_o)

    return valid_json_answer


@pytest.fixture
def email():
    email = ['k.bx@ya.ru', 'eehzntm5@hotmail.com', 'manuruel@yahoo.com', 'russellebb912@hotmail.com',
             'jnkitchener@btinternet.com', 'ras-nie@web.de', 'ghagen4@gmail.com', 'mattdhoey@gmail.com']
    return email
