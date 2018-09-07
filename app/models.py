from . import db
from flask_sqlalchemy import SQLAlchemy
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
    content = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)
    dislikes = db.Column(db.Integer, nullable=False)
    time = db.Column(db.DateTime, default=datetime.utcnow)
    author_id = db.Column(
        db.Integer, db.ForeignKey('users.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey(
        'categories.id'), nullable=False)
    comment_id = db.Column(db.Integer, db.ForeignKey(
        'comments.id'), nullable=False)

    def __repr__(self):
        return f'Pitch {self.title}, {self.content}, {self.rating}, {self.likes}, {self.dislikes}, {self.time}'


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    bio = db.Column(db.String, nullable=False)
    photo = db.Column(db.String, default='default.jpg')
    password_hash = db.Column(db.String(60), nullable=False)
    pitches = db.relationship('Pitch', backref='author', lazy='dynamic')
    comments = db.relationship('Comment', backref='author', lazy='dynamic')

    def __repr__(self):
        return f'User {self.name}, {self.photo}, {self.bio}'


class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    rating = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)
    dislikes = db.Column(db.Integer, nullable=False)
    author_id = db.Column(
        db.Integer, db.ForeignKey('users.id'), nullable=False)
    pitch = db.relationship('Pitch', backref='comment', lazy='dynamic')

    def __repr__(self):
        return f'Comment {self.content}, {self.time}, {self.rating}, {self.likes}, {self.dislikes}'
