from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_limiter import Limiter
from app.utils.error_handlers import error_handlers_blueprint
from os import getenv
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configuration from .env
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{getenv('MYSQL_USER')}:{getenv('MYSQL_PASSWORD')}@{getenv('MYSQL_HOST')}:{getenv('MYSQL_PORT')}/{getenv('MYSQL_DB')}"

db = SQLAlchemy(app)
jwt = JWTManager(app)
limiter = Limiter(app, key_func=get_remote_address) # Rate limiting

# Register blueprints
app.register_blueprint(error_handlers_blueprint)






