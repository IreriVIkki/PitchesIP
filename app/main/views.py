from flask import render_template, url_for
from . import main


@main.route('/')
def home():
    title = 'Welcome To Pitches'
    return render_template('index.html', title=title)
