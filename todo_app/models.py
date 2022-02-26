import json
from flask_sqlalchemy import SQLAlchemy
from flask import abort

db = SQLAlchemy()


class TodoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todos = db.relationship("Todo", backref="todo_list", lazy=True)

    @staticmethod
    def create():
        todo_list = TodoList()
        db.session.add(todo_list)
        db.session.commit()

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

