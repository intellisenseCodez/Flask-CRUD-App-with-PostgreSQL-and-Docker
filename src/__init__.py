from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config


# instance flask
app = Flask(__name__)
app.config.from_object(Config)


# instace for SQLAlchemy
db = SQLAlchemy(app)

migrate = Migrate(app, db)


from src.books import routes, models
