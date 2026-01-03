from repository import add_user, list_users


def create_user(name):
    print("Service creating user")
    user = {"name": name}
    return add_user(user)


def get_users(name=None):
    print("Service getting user")
    return list_users(name)