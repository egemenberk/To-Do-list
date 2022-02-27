from models import User, TodoList, Todo, db
from schema import TodoSchema, TodoListSchema

# Add authentication per User
todo_schema = TodoSchema()
todo_list_schema = TodoListSchema()


def create_todo(todo):
    # Get TodoList from user
    todo_list = TodoList.query.filter(TodoList.id == 1).first()
    new_todo = Todo(todo_list_id=todo_list.id, **todo)
    db.session.add(new_todo)
    db.session.commit()
    return todo_schema.jsonify(new_todo)


def get_todo_items(user, id=None):
    todo_items = Todo.query.filter().all()
    return TodoSchema(many=True).jsonify(todo_items)


def get_todo_list_items(user):
    todo_list_items = TodoList.query.filter().all()
    return TodoListSchema(many=True).jsonify(todo_list_items)


def delete_todo(todo_id):
    Todo.delete_todo(todo_id)


def complete_todo(todo_id):
    Todo.complete_todo(todo_id)


def create_user(user):
    new_user = User(**user)
    db.session.add(new_user)
    db.session.commit()


def create_todo_list(user):
    todo_list = TodoList.create(user)
    return todo_list_schema.jsonify(todo_list)
