import factory

from todo_app import models
from werkzeug.security import generate_password_hash


class UserFactory(factory.Factory):
    class Meta:
        model = models.User
    username = "Test"
    password = generate_password_hash("pass")


class TodoListFactory(factory.Factory):
    class Meta:
        model = models.TodoList
    user = factory.SubFactory(UserFactory)


class TodoFactory(factory.Factory):
    class Meta:
        model = models.Todo
    text = "test"
    completed = False
    todo_list = factory.SubFactory(TodoListFactory)
