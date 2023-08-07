from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from os import getenv
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configuration from .env
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{getenv('MYSQL_USER')}:{getenv('MYSQL_PASSWORD')}@{getenv('MYSQL_HOST')}:{getenv('MYSQL_PORT')}/{getenv('MYSQL_DB')}"

db = SQLAlchemy(app)
jwt = JWTManager(app)

