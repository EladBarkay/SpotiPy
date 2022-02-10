import random
import string


def generate(length: int):
    _all = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return "".join(random.sample(_all, length))
