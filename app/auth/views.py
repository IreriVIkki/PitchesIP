from flask import render_template, redirect, url_for, flash
from . import auth
from .forms import LoginForm, RegistrationForm
from ..models import db, User
from flask_login import login_user, logout_user


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('main.dashboard'))
        else:
            flash('Invalid login credentials')
    return render_template('auth/login.html', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, name=form.username.data,
                    password=form.password.data)
        user.save_user(user)
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title='Register', form=form)


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))
