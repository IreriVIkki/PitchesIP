from . import db
from flask_sqlalchemy import SQLAlchemy, orm
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from flask_login import login_user


class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)
    time = db.Column(db.String(100))
    rating = db.Column(db.Integer)
    likes = db.Column(db.Integer)
    dislikes = db.Column(db.Integer)
    bs = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))

    def save_comment(self, comment):
        db.session.add(comment)
        db.session.commit()

    def __repr__(self):
        return f'Comment ({self.content}, {self.time}, {self.rating}, {self.likes}, {self.dislikes})'


class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    rating = db.Column(db.Integer)
    likes = db.Column(db.Integer)
    dislikes = db.Column(db.Integer)
    time = db.Column(db.String)
    category_id = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comments = db.relationship('Comment', backref='pitch', lazy='dynamic')

    def save_pitch(self, pitch):
        db.session.add(pitch)
        db.session.commit()

    def __repr__(self):
        return f'Pitch ({self.title}, {self.content}, {self.rating}, {self.likes}, {self.dislikes}, {self.time})'


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    bio = db.Column(db.String)
    photo = db.Column(db.String, default='default.jpg')
    password_hash = db.Column(db.String(255))
    pitches = db.relationship('Pitch', backref='author', lazy='dynamic')
    comments = db.relationship('Comment', backref='author', lazy='dynamic')

    def save_user(self, user):
        db.session.add(user)
        db.session.commit()

    @property
    def password(self):
        raise AttributeError('You cant read password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'User ({self.name}, {self.email}, {self.bio})'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
