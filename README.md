
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
```

Connect to postgres and create database
```bash
psql
create database todo_list;
exit
```

Set up python requirements
```bash
export FLASK_APP=todo_app/app.py
flask db init
flask db migrate
flask db upgrade
```

# Running app
```bash
chmod +x run.sh
./run.sh
```
Open http://127.0.0.1:5000/ui/ and test the app by first creating a user via ui

# Running tests
```bash
pytest tests/
```

# Todos of the project
requirements.txt does not include versions, which might introduce dependency issues later on

