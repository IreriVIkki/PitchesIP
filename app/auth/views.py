from flask import render_template
from . import auth
from .forms import LoginForm, RegisterForm


@auth.route('/login')
def login():
    form = LoginForm()
    return render_template('auth/login.html', form=form)


@auth.route('/register')
def register():
    form = RegisterForm()
    return render_template('auth/register.html', form=form)
