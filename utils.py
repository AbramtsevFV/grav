import hashlib

import requests


def get_result(res, email):
    """Обрабатываем результаты полученные от сервера
    на выходе получаем с заданными параметрами"""
    result = {
        "result": {
            'id': res.get('entry', [{}])[0].get('id', None),
            'email_hash': res.get('entry', [{}])[0].get('hash', None),
            'email': email,
            'url': res.get('entry', [{}])[0].get('profileUrl', None),
            'alias': res.get('entry', [{}])[0].get('preferredUsername', None),
            'photos': res.get('entry', [{}])[0].get('photos', [{}])[0].get('value', None),
            'person': res['entry'][0]['name']['formatted'] if 'formatted' in res['entry'][0]['name'] else None,
            'location': res.get('entry', [{}])[0].get('currentLocation', None),
            'accounts': res.get('entry', [{}])[0].get('accounts', [{}])[0].get('url', None),
            'urls': res.get('entry', [{}])[0].get('urls', None)

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
    if res.status_code == 200 or res.json() == "User not found":
        r = res.json()
        if r != "User not found":
            return get_result(r, email)
        return {"message": f"The user with the email {email}  was not found"}
    return {"message": f"Connection error. Status code {res.status_code}"}
