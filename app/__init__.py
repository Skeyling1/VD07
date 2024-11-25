# настройки фласка

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' #это имя файла базы данных, который будет создан в корневом каталоге проекта

db = SQLAlchemy(app)
bcrypt = Bcrypt(app) #для безопасного хэширования паролей

login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Модуль будет перенаправлять пользователя на маршрут, который мы указываем (на авторизацию)

from app import routes

