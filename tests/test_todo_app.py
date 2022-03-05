from requests.auth import _basic_auth_str
from todo_app.models import Todo, TodoList, User

from tests.factory import TodoFactory, TodoListFactory, UserFactory


def test_auth_fails_without_correct_username(test_client, user, _user):
    _user["username"] = "changed username"
    headers = {
        "Authorization": _basic_auth_str(**_user),
    }
    response = test_client.get("todos", headers=headers)
    assert response.status_code == 401


def test_auth_fails_without_correct_password(test_client, user, _user):
    _user["password"] = "changed pass"
    headers = {
        "Authorization": _basic_auth_str(**_user),
    }
    response = test_client.get("todos", headers=headers)
    assert response.status_code == 401


def test_create_todo_list(session, test_client, user):
    response = test_client.post("todo-lists")
    assert response.status_code == 201
    assert TodoList.query.all()[0].id == response.json["id"]


def test_create_todo(session, test_client, user, todo_list):
    response = test_client.post(
        "todos", json={"todo_list_id": todo_list.id, "text": "text", "completed": False}
    )
    assert response.status_code == 201
    assert Todo.query.all()[0].id == response.json["id"]


def test_get_todo_lists_for_user(session, test_client, user, todo_list):
    response = test_client.get("todo-lists")
    assert response.status_code == 200
    assert todo_list.id == response.json[0]["id"]


def test_get_todos_for_user(session, test_client, user, todo):
    response = test_client.get("todos")
    assert response.status_code == 200
    assert todo.id == response.json[0]["id"]


def test_complete_todo(session, test_client, user, todo):
    assert todo.completed != True
    response = test_client.post(f"todos/{todo.id}/complete")
    assert response.status_code == 204
    assert todo.completed == True


def test_delete_todo(session, test_client, user, todo):
    assert len(Todo.query.all()) > 0
    response = test_client.delete(f"todos/{todo.id}")
    assert response.status_code == 204
    assert len(Todo.query.all()) == 0


def test_delete_todo(session, test_client, user, todo):
    assert len(Todo.query.all()) > 0
    response = test_client.delete(f"todos/{todo.id}")
    assert response.status_code == 204
    assert len(Todo.query.all()) == 0


def test_delete_not_existing_todo(session, test_client, user, todo):
    assert len(Todo.query.all()) > 0
    response = test_client.delete(f"todos/{99999}")
    assert response.status_code == 404
