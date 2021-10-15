import json

import pytest


@pytest.fixture(scope="session")
def result():
    with open("tests/result.json", 'r') as f_o:
        valid_json_answer = json.load(f_o)

    return valid_json_answer
