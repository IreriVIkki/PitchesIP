from flask import render_template, url_for, redirect
from .forms import RegisterForm, LoginForm
from . import auth
from .. import db
from ..models import User


@auth.route('/login')
def login():
    form = LoginForm()
    return render_template('auth/login.html', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        print('WORKS')
        user = User(email=form.email.data, name=form.name.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)
