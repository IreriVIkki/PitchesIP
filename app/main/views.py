from flask_login import login_required
from flask import render_template, url_for, redirect
from . import main
from .forms import PitchForm, CommentForm
from flask_login import current_user
from ..models import Pitch, Comment, User
from datetime import datetime
from flask_wtf import FlaskForm
import markdown2


@main.route('/', methods=['GET', 'POST'])
def home():
    title = 'Welcome To Pitches'
    pitchesa = Pitch.query.all()
    all_pitches = len(pitchesa)
    pitches = sub_arrays(pitchesa, 4)
    return render_template('index.html', title=title, pitches=pitches, all_pitches=all_pitches)


@main.route('/comments/<id>', methods=['GET', 'POST'])
@login_required
def click(id):
    title = "Please leave a comment"
    pitch = Pitch.query.get(id)
    form = CommentForm()
    user = current_user
    comments = len(pitch.comments.all())
    if form.validate_on_submit():
        new_comment = Comment(content=form.content.data,
                              time=datetime.utcnow().strftime("%H:%M"),
                              rating=0,
                              likes=0,
                              dislikes=0,
                              author=user,
                              pitch=pitch)
        new_comment.save_comment(new_comment)
        print(new_comment)

        return redirect(url_for('main.click', id=id))

    return render_template('comment.html', title=title,  form=form, pitch=pitch, comments=comments)


@main.route('/<uname>/new/pitch', methods=['GET', 'POST'])
@login_required
def new_pitch(uname):

    form = PitchForm()
    if form.validate_on_submit():
        print(form.category.data)
        new_pitch = Pitch(title=form.title.data,
                          content=form.content.data,
                          rating=0,
                          likes=0,
                          dislikes=0,
                          time=datetime.utcnow().strftime("%H:%M"), category_id=form.category.data,
                          author=current_user
                          )
        new_pitch.save_pitch(new_pitch)

        return redirect(url_for('main.home'))
    return render_template('pitch.html', form=form, title='Create New Pitch')


@main.route('/<user>/dashboard')
@login_required
def dashboard(user):
    pitches = Pitch.query.all()
    all_pitches = len(pitches)
    return render_template('dashboard.html', title='Dashboard', pitches=pitches, all_pitches=all_pitches)


def sub_arrays(array, num):
    start = 0
    main_list = []
    while start < len(array):
        start2 = start
        arr2 = []
        for i in range(num):
            arr2.append(array[start2+i])
            if (start2+i) == (len(array)-1):
                break
        # print(articles)
        main_list.append(arr2)
        start += num
    return main_list


def delete_pitch(id):
    pitch = Pitch.query.get(id)
    Pitch.query.all().remove(pitch)
