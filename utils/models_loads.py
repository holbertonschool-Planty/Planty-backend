from django.apps import apps

def get_users_model():
    return apps.get_model("Users", "Users")


def get_usersToken_model():
    return apps.get_model("Users", "UserToken")