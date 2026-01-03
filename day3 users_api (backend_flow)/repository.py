users = []


def add_user(user):
    print("Repo saving user")
    users.append(user)
    return user


def list_users(name=None):
    print("Repo fetching user")
    if name:
        return [u for u in users if u["name"] == name]
    return users