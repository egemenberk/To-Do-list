from models import User
from flask import abort

def basic_auth(username, password, required_scopes=None):
    user = User.query.filter(User.username == username).one_or_none()
    if user:
        if user.verify_password(password):
            return {"sub": user}
    return None

