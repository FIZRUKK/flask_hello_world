# Импортируем класс Flask из модуля flask
from flask import Flask

# Создаем экземпляр приложения Flask
app = Flask(__name__)

# Декоратор route используется для указания URL, по которому будет доступна функция
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Если данный файл запускается напрямую (а не импортируется как модуль),
# запускаем веб-сервер Flask
if __name__ == '__main__':
    app.run()
