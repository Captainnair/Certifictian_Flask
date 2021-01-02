from flaskapp import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.id}', '{self.username}', '{self.email}')"


class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(), unique=True, nullable=False)
    choice1 = db.Column(db.String(), nullable=False)
    choice2 = db.Column(db.String(), nullable=False)
    choice3 = db.Column(db.String(), nullable=False)
    choice4 = db.Column(db.String(), nullable=False)
    answer = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"Questions('{self.id}', '{self.question}', '{self.answer}')"
