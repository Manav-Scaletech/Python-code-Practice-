import pytest
# Import the components from your permissions.py file
from permissions import User, is_user_allowed, ForbiddenException


def test_user_not_allowed():
    """Verifies that a standard user causes the application to raise an exception."""
    # 1. Create a user who is NOT an admin
    user = User(is_admin=False)
    
    # 2. Tell pytest to expect a ForbiddenException crash here
    with pytest.raises(ForbiddenException):
        is_user_allowed(user)


def test_admin_allowed():
    """Verifies that an admin user passes through successfully without crashing."""
    # 1. Create a user who IS an admin
    user = User(is_admin=True)
    
    # 2. Run the function
    result = is_user_allowed(user)
    
    # 3. Assert that the function returned True
    assert result is True
