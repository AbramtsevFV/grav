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
            'photos': res.get('entry', [{}])[0].get('preferredUsername', [{}])[0].get('value', None),
            'person': res.get('entry', [{}])[0].get('name', {}).get('formatted', None) ,
            'location': res['entry'][0]['currentLocation'] if 'currentLocation' in res['entry'][0] else None,
            'accounts': res['entry'][0]['accounts'][0]['url'] if 'accounts' in res['entry'][0] else None,
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
    if res.status_code == 200:
        r = res.json()
        if r != "User not found":
            return get_result(r, email)
        return {"message": f"The user with the email {email}  was not found"}
    return {"message": f"Connection error. Status code {res.status_code}"}
