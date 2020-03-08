from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_bcrypt import Bcrypt

from .filesystem import templates_path
from .db_config import DBConfig

params = {"template_folder": templates_path}

application = Flask(__name__, **params)

application.config.from_object(DBConfig)
db = SQLAlchemy(application)

bcrypt = Bcrypt(application)
