from . import db
from datetime import datetime


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(20), unique=True, nullable=False)
    pitches = db.relationship('Pitch', backref='category', lazy='dynamic')

    def __repr__(self):
        return f'Category {self.category_name}'


class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String, nullable=False)
    rating = db.Column(db.Interger, nullable=False)
    likes = db.Column(db.Integer, nullable=False)
    dislikes = db.Column(db.Integer, nullable=False)
    time = db.Column(db.DateTime, default=datetime.utcnow)
    author_id = db.Column(db.Interger, db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    comment_id = db.Column(db.Integer, db.ForeignKey('comments.id'))

    def __repr__(self):
        return f'Pitch {self.title}, {self.content}, {self.rating}, {self.likes}, {self.dislikes}, {self.time}'
