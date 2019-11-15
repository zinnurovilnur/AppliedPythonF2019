# TODO: код где-нибудь здесь. Если есть желание, можно и на ином языке.
# Требуется создать ручку с произвольным именем, которое вы в последствии передадите на мой сервис для проверки.
# В обработчике ручки необходимо кинуть запрос на auth сервис и получить информацию о себе
# с помощью ручки about_me (авторизация по кукам).
# Вернуть json в котором указать username, age и sale, которая рассчитывается по формуле round(age / 7).
# Кука при запросе на сервис auth должна быть вида
# {'session': '<длинный id>', 'technoatom': '<длинный id2>'}, её можно получить из запроса к сервису.

import requests

from flask import Flask, request, jsonify

from flask_login import (
    LoginManager
)

# python3.7 server.py
HOST = '0.0.0.0'

app = Flask(__name__)
app.config["SECRET_KEY"] = "123SECRET_KEY123"
app.config['REMEMBER_COOKIE_NAME'] = 'technoatom'

login_manager = LoginManager()


@app.route('/sale')
def sale():
    technoatom = request.cookies.get('technoatom')
    session = request.cookies.get('session')

    r = requests.get('https://auth:5000/about_me', params=jsonify(technoatom, session))
    name = '\n'.join(i['name'] for i in r)
    age = '\n'.join(i['age'] for i in r)
    salo = int(age) / 7
    return jsonify(name=name, age=age, sale=salo)


def main():
    app.run(host=HOST, debug=True, port=8000)


if __name__ == '__main__':
    main()
