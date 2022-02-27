import json
from werkzeug.security import generate_password_hash, check_password_hash
from flask import abort
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class TodoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todos = db.relationship("Todo", backref="todo_list", lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)

    def __init__(self, user_id):
        self.user_id = user_id

    @staticmethod
    def create(user):
        todo_list = TodoList(user_id=user.id)
        db.session.add(todo_list)
        db.session.commit()
        return todo_list

    @staticmethod
    def add_todo(todo_list_id, text, completed=False):
        todo = Todo(todo_list_id, text, completed)
        db.session.add(todo)
        db.session.commit()


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String())
    completed = db.Column(db.Boolean())
    todo_list_id = db.Column(db.Integer, db.ForeignKey("todo_list.id"), nullable=True)

    def __init__(self, todo_list_id, text, completed=False):
        self.todo_list_id = todo_list_id
        self.text = text
        self.completed = completed

    @staticmethod
    def get_all_items():
        return [str(todo) for todo in Todo.query.all()]

    def __repr__(self):
        todo = {
            'id': self.id,
            'text': self.text,
            'completed': self.completed,
        }
        return json.dumps(todo)

    @staticmethod
    def delete_todo(todo_id):
        todo = Todo.query.filter(Todo.id == todo_id).one_or_none()
        if todo:
            db.session.delete(todo)
            db.session.commit()
        else:
            abort(404, f"Todo item with id: {todo_id} is not found")

    @staticmethod
    def complete_todo(todo_id):
        todo = Todo.query.filter(Todo.id == todo_id).one_or_none()
        if todo:
            todo.completed = True
            db.session.commit()
        else:
            abort(404, f"Todo item with id: {todo_id} is not found")


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120))
    todo_lists = db.relationship("TodoList", backref="user", lazy=True)


    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)
    
    def __repr__(self):
        return f'<User {self.username}>'

    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)
