from todo_app.models import Todo, TodoList, User
from requests.auth import _basic_auth_str


def test_auth_fails_without_correct_username(session, test_client, _logged_in_user):
    _logged_in_user["username"] = "changed username"
    headers = {
        "Authorization": _basic_auth_str(**_logged_in_user),
    }
    response = test_client.get("todo", headers=headers)
    assert response.status_code == 401


def test_auth_fails_without_correct_password(session, test_client, _logged_in_user):
    _logged_in_user["password"] = "changed pass"
    headers = {
        "Authorization": _basic_auth_str(**_logged_in_user),
    }
    response = test_client.get("todo", headers=headers)
    assert response.status_code == 401


def test_auth_fails_without_headers(session, test_client, _logged_in_user):
    response = test_client.get("todo")
    assert response.status_code == 401
