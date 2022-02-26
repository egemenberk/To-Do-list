# To-Do-list
Run the following commands to start the app

mkvirtualenv todo-list-api -p $(which python3)
setvirtualenvproject
flask db init
flask db migrate
flask db upgrade


# DownSides of the project
requirements.txt does not include versions, which might introduce dependency issues
