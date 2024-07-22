import os

class Config:
    APP_NAME = "MyApp"
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'supersecretkey'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME") or "admin"
    ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD") or "password"