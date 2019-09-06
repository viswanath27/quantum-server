from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '8bedc6ccbfbb7d71d2654b1fa280189a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/quantumDatabase.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from quantumserver import routes