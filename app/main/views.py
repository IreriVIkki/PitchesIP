from flask_login import login_required
from flask import render_template, url_for
from . import main
from flask_login import current_user


@main.route('/')
def home():
    title = 'Welcome To Pitches'
    return render_template('index.html', title=title)


@main.route('/new/pitch')
@login_required
def new_pitch():
    return render_template('pitch.html', title='Create New Pitch')


@main.route('/user/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', title='Dashboard')
