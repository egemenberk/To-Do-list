
# Setting Up
```bash
mkvirtualenv todo-list-api -p $(which python3)
setvirtualenvproject
flask db init
flask db migrate
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

