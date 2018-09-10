from flask_login import login_required
from flask import render_template, url_for, redirect
from . import main
from .forms import PitchForm, CommentForm
from flask_login import current_user
from ..models import Pitch, Comment, Category, User
from datetime import datetime


@main.route('/')
def home():
    title = 'Welcome To Pitches'
    return render_template('index.html', title=title)


@main.route('/<uname>/new/pitch', methods=['GET', 'POST'])
@login_required
def new_pitch(uname):
    form = PitchForm()

    if form.validate_on_submit():
        return redirect(url_for('main.home'))
    return render_template('pitch.html', form=form, title='Create New Pitch')


@main.route('/<user>/dashboard')
@login_required
def dashboard(user):
    return render_template('dashboard.html', title='Dashboard')
