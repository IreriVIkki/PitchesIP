from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, TextField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length


class PitchForm(FlaskForm):
    title = StringField('Pitch title', validators=[
                        DataRequired(), Length(min=2, max=20)])
    content = TextAreaField('Enter Pitch Here', validators=[
        DataRequired, Length(min=2, max=20)])
    category = SelectField('Category', choices=[
                           ('Art', 'Art'), ('Business', 'Business'), ('Medicine', 'Medicine'), ('Music', 'Music')])
    submit = SubmitField('Publish')


class CommentForm(FlaskForm):
    content = TextAreaField('Add a comment', validators=[DataRequired()])
