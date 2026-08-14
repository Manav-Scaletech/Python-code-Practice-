class ForbiddenException(Exception):
    pass


class User:
    def __init__(self, is_admin):
        self.is_admin = is_admin


def is_user_allowed(user):

    if user.is_admin:
        return True

    raise ForbiddenException("User is not an admin")