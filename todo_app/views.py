from todo_app.models import User, TodoList, Todo, db
from todo_app.schema import TodoSchema, TodoListSchema
from flask import abort

todo_schema = TodoSchema()
todo_list_schema = TodoListSchema()


def create_todo(todo, user):
    todo_list_id = todo.get("todo_list_id")
    todo_list = TodoList.query.filter(TodoList.id == todo_list_id).one_or_none()
    if not todo_list:
        abort(404, f"TodoList item with id: {todo_list_id} is not found")
    new_todo = Todo(**todo)
    db.session.add(new_todo)
    db.session.commit()
    return todo_schema.jsonify(new_todo), 201


def get_todo_items(user, id=None):
    todo_items = TodoList.get_todo_items_for_user(user)
    return TodoSchema(many=True).jsonify(todo_items)


def get_todo_list_items(user):
    todo_list_items = TodoList.query.filter().all()
    return TodoListSchema(many=True).jsonify(todo_list_items)


def delete_todo(todo_id, user):
    # CRITICAL
    # TODO add permission check if todo belongs to the user
    Todo.delete_todo(todo_id)


def complete_todo(todo_id, user):
    Todo.complete_todo(todo_id)


def create_user(user):
    new_user = User(**user)
    db.session.add(new_user)
    db.session.commit()


def create_todo_list(user):
    todo_list = TodoList.create(user)
    return todo_list_schema.jsonify(todo_list), 201
