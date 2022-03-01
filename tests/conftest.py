# This conftest.py is fetched from http://alexmic.net/flask-sqlalchemy-pytest/

import os
import pytest

from todo_app.app import create_app
from tests.factory import UserFactory
from todo_app.models import db as _db
from flask.testing import FlaskClient

from requests.auth import _basic_auth_str
from todo_app.views import create_user
from todo_app.models import Todo, TodoList


TESTDB = "test_project.db"
TESTDB_PATH = "./{}".format(TESTDB)
TEST_DATABASE_URI = "sqlite:///" + TESTDB_PATH


@pytest.fixture(scope="session")
def app(request):
    """Session-wide test `Flask` application."""
    settings_override = {"TESTING": True, "SQLALCHEMY_DATABASE_URI": TEST_DATABASE_URI}
    app = create_app(settings_override)

    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app


@pytest.fixture(scope="session")
def db(app, request):
    """Session-wide test database."""
    if os.path.exists(TESTDB_PATH):
        os.unlink(TESTDB_PATH)

    def teardown():
        _db.drop_all()
        if os.path.exists(TESTDB_PATH):
            os.unlink(TESTDB_PATH)

    _db.app = app
    _db.create_all()

    request.addfinalizer(teardown)
    return _db


@pytest.fixture(scope="function")
def session(db, request):
    """Creates a new database session for a test."""
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session

    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)
    return session

@pytest.fixture(scope="session")
def _user():
    return {"username": "test", "password": "pass"}


@pytest.fixture(scope="function")
def user(session, _user):
    new_user = UserFactory(**_user)
    session.add(new_user)
    session.commit()
    return new_user


@pytest.fixture(scope="function")
def test_client(app, user, _user):
    client = app.test_client()
    client.environ_base['HTTP_AUTHORIZATION'] = _basic_auth_str(**_user)
    return client


@pytest.fixture(scope="function")
def todo_list(session, user):
    new_todo_list = TodoList(user_id=user.id)
    session.add(new_todo_list)
    session.commit()
    return new_todo_list


@pytest.fixture(scope="function")
def todo(session, user, todo_list):
    new_todo = Todo(todo_list_id=todo_list.id, text="test")
    session.add(new_todo)
    session.commit()
    return new_todo

