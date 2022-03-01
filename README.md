
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
cd to-do-list
mkvirtualenv todo-list-api -p $(which python3)
setvirtualenvproject
```

Connect to postgres and create database
```bash
psql
# create database todo_list;
# exit
flask db upgrade
```
# Running app
```bash
chmod +x run.sh
./run.sh
```

# Running tests
```bash
pytest tests/
```

# Todos of the project
requirements.txt does not include versions, which might introduce dependency issues later on

