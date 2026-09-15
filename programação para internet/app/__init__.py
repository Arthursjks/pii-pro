from flask import Flask
from flask_wtf import CSRFProtect
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
csrf = CSRFProtect(app) # Protege os formulários contra ataques CSRF

from app.models.usuarios import Usuario

with app.app_context():
    db.create_all()

from app import routes


