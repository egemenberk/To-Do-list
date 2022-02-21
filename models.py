from app import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String())
    completed = db.Column(db.Boolean())

    def __init__(self, text, completed=False):
        self.text = completed
        self.completed = completed
