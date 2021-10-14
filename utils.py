import hashlib

import requests


def get_result(res, email):
    """Обрабатываем результаты полученные от сервера
    на выходе получаем с заданными параметрами"""
    result = {
        "result": {
            'id': res['entry'][0]['id'],
            'email_hash': res['entry'][0]['hash'],
            'email': email,
            'url': res['entry'][0]['profileUrl'],
            'alias': res['entry'][0]['preferredUsername'],
            'photos': res['entry'][0]['photos'][0]['value'],
            'person': res['entry'][0]['name']['formatted'] if res['entry'][0]['name'] else None,
            'location': res['entry'][0]['currentLocation'] if 'currentLocation' in res['entry'][0] else None,
            'accounts': res['entry'][0]['accounts'][0]['url'] if 'accounts' in res['entry'][0] else None,
            'urls': res['entry'][0]['urls']

        }
    }
    return result


def get_hash(email):
    """Получаем hash email из запроса"""
    return hashlib.md5(email.encode()).hexdigest()


def get_req(email):
    """ Запрос к серверу API и возврат результата"""
    url = f"https://ru.gravatar.com/{get_hash(email)}.json"
    session = requests.Session()
    res = session.get(url)
    if res.status_code == 200:
        r = res.json()
        if r != "User not found":
            return get_result(r, email)
        return {"message": f"The user with the email {email}  was not found"}
    return {"message": f"Connection error. Status code {res.status_code}"}
