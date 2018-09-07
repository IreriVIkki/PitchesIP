from flask_login import login_required
from flask import render_template, url_for
from . import main


@main.route('/')
def home():
    title = 'Welcome To Pitches'
    return render_template('index.html', title=title)


@main.route('/new/pitch')
@login_required
def new_pitch():
    pass
