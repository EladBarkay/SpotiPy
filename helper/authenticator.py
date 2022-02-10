import os
import objects.user


def login(username: str):
    """
    just logs in if the user exists. no authenticating - YET
    :param username:
    :return: User instance of the specific user
    """
    return objects.user.load(username)
