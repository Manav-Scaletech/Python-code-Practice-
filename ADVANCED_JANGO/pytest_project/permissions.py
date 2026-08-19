class ForbiddenException(Exception):
    """Custom error raised when a non-admin tries to gain access."""
    pass


class User:
    """Represents a user in the system."""
    def __init__(self, is_admin: bool):
        self.is_admin = is_admin


def is_user_allowed(user: User) -> bool:
    """Checks if the user has permission.
    
    Raises a ForbiddenException if the user is not an admin.
    """
    if not user.is_admin:
        raise ForbiddenException("Access Denied: User is not an admin.")
    
    return True
