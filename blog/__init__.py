from dotenv import load_dotenv
import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from blog import routes, models, forms

@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Entry": models.Entry}