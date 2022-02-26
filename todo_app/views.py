from models import TodoList, Todo
from schema import TodoSchema


def create_todo(text, todo_list_id=None):
    if not todo_list_id:
        todo_list_id = 2
    TodoList.add_todo(text, todo_list_id)


def get_todo_items(id=None):
    todo_items = Todo.query.filter().all()
    return TodoSchema(many=True).jsonify(todo_items)


