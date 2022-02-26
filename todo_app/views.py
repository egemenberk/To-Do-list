from models import TodoList, Todo, db
from schema import TodoSchema

# Add authentication per User

def create_todo(todo):
    # Get TodoList from user
    todo_list = TodoList.query.filter(TodoList.id == 1).first()
    new_todo = Todo(todo_list_id=todo_list.id, **todo)
    todo_schema = TodoSchema()
    db.session.add(new_todo)
    db.session.commit()
    return todo_schema.jsonify(new_todo)


def get_todo_items(id=None):
    todo_items = Todo.query.filter().all()
    return TodoSchema(many=True).jsonify(todo_items)


def delete_todo(todo_id):
    Todo.delete_todo(todo_id)
