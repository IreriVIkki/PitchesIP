from flask_login import login_required
from flask import render_template, url_for
from . import main
from .forms import PitchForm
from flask_login import current_user


@main.route('/')
def home():
    title = 'Welcome To Pitches'
    return render_template('index.html', title=title)


@main.route('/new/pitch', methods=['GET', 'POST'])
@login_required
def new_pitch():
    form = PitchForm()

    return render_template('pitch.html', form=form, title='Create New Pitch')


@main.route('/user/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', title='Dashboard')
