from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Email, Length, DataRequired


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Email(), DataRequired()])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=3, max=20)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Submit')


class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[Email(), DataRequired()])
    username = StringField('Username', validators=[
                           Length(min=2, max=20), DataRequired()])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=3, max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(), Length(min=3, max=20)])
    submit = SubmitField('Register')
