

def basic_auth(username, password, required_scopes=None):
    if username == 'admin' and password == 'secret':
        return {'sub': 'admin'}

    # optional: raise exception for custom error response
    return None


def get_secret(user) -> str:
    return f"You are {user} and the secret is 'wbevuec'"
