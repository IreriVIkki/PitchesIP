from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import Email, Length, DataRequired
from ..models import User


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

    def validate_email(self, data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self, data_field):
        if User.query.filter_by(name=data_field.data).first():
            raise ValidationError('That user name is taken')
