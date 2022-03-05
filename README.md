
# Setting Up

## Prerequisites
Install postgresql to you machine
Install python3.8 or above in your local and set that as global python3 version

```bash
pip install virtualenvwrapper
git clone git@github.com:egemenberk/To-Do-list.git
```

## Install
```bash
cd To-Do-list
mkvirtualenv todo-list-api -p $(which python3) -r requirements.txt
setvirtualenvproject
export FLASK_APP=todo_app/app.py
```

## Creating database
```bash
psql
create database todo_list;
exit
```

## Create tables
```bash
python
from todo_app.models import db
from wsgi import app

with app.app_context():
    db.create_all()
```

# Running app locally
```bash
chmod +x run.sh
./run.sh
```

Open http://127.0.0.1:5000/ui/ and test the app by first creating a user via ui

# Deploying on heroku
First, create an account and create an app

```bash
heroku addons:create heroku-postgresql:hobby-dev --app <APP_NAME_HERE>
heroku run python
```
Then create tables in remote database as well by doing steps in [here](#create-tables)

# Running tests
```bash
pytest tests/
```

# Todos of the project
- For easiness of usage, swagger UI is enabled by default, swagger UI can have its own db and run on another machine seperated from real API service
- requirements.txt does not include versions, which might introduce dependency issues later on
- Integration of factory classes with database is problematic, fix that to utilize testing tools better

