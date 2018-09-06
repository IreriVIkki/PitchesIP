from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Email, Length, Required


class LoginForm(FlaskForm):
    username = StringField('Email', validators=[Email()])
    password = PasswordField('Password', validators=[
                             Required(), Length(min=3, max=20)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Submit')


class RegisterForm(FlaskForm):
    pass
