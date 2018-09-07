from flask import render_template, redirect, url_for
from . import auth
from .forms import LoginForm, RegistrationForm
from ..models import db, User


@auth.route('/login')
def login():
    return render_template('auth/login.html')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, name=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.home'))
    return render_template('auth/register.html', title='Register', form=form)
