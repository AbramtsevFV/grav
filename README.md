# grav
## Задание ##
Необходимо написать python скрипт, который на входе будет принимать параметр query (в него будем передавать емейл), а на выходе мы должны выдать json следующего формата:
``
  {
  "result": {....}
  }
``

В result мы можем поместить ответ от gravatar, но с изменениям по именованию полей:

```
  id -> id
  hash -> email_hash
  profileUrl -> url
  preferredUsername -> alias
  thumbnailUrl -> thumb
  photos -> photos
  name.formatted -> person
  currentLocation -> location
  emails -> emails
  accounts -> accounts
  urls -> urls
```
Примеры емейлов:
```
  eehzntm5@hotmail.com
  manuruel@yahoo.com
  russellebb912@hotmail.com
  jnkitchener@btinternet.com
  ras-nie@web.de
  ghagen4@gmail.com
  mattdhoey@gmail.com
  ```
  ## Установка ##
  Для установки нужно выполнить команду в консоли (должен быть предварительно установлени Python  3.8:
  Команда для Linux:
    
    ```
    git clone https://github.com/AbramtsevFV/grav && cd ./grav && python3.8 -m venv venv && source ./venv/bin/activate && pip install -r requirements.txt &&  python app.py
    ```
 ## Работа ##
 Отправьте GET запрос с параметрами:
 
>  http://127.0.0.1:5000/grav?q=email

 где email это email пользователя сервиса gravatar.com
 ***
 Пример запроса из командной строки:
 ```
    curl http://127.0.0.1:5000/grav?q=mattdhoey@gmail.com
  ```
 ## Тесты ##
 Для запуска тестов откройте консоль в корневой деректории с GRAV и выполните команду:
 Команда для Linux:
 ```
  source venv/bin/activate && pytest tests -v
  ```
