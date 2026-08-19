import pytest
from permissions import User, is_user_allowed, ForbiddenException

def test_user_not_allowed():
    user = User(is_admin=False)
    # Pytest watches for the crash here. If it crashes as expected, the test PASSES.
    with pytest.raises(ForbiddenException):
        is_user_allowed(user)

def test_admin_allowed():
    user = User(is_admin=True)
    result = is_user_allowed(user)
    assert result is True
