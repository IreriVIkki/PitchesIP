from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, TextField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length


class PitchForm(FlaskForm):
    title = StringField('Pitch title', validators=[
                        DataRequired(), Length(max=50)])
    content = TextField('Enter Pitch Here', Length(min=5))
    category = SelectField('Category')
    submit = SubmitField('Publish')
