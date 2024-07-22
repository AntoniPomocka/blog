from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, ValidationError
from config import Config

class EntryForm(FlaskForm):
    title = StringField('Tytuł', validators=[DataRequired()])
    body = TextAreaField('Treść', validators=[DataRequired()])
    is_published = BooleanField('Opublikowany')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

    def validate_username(self, field):
        if field.data != Config.ADMIN_USERNAME:
            raise ValidationError("Invalid username")

    def validate_password(self, field):
        if field.data != Config.ADMIN_PASSWORD:
            raise ValidationError("Invalid password")