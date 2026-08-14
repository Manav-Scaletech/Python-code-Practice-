import pytest

from permissions import User
from permissions import is_user_allowed
from permissions import ForbiddenException


def test_user_not_allowed():

    user = User(is_admin=False)

    with pytest.raises(ForbiddenException):
        is_user_allowed(user)


def test_admin_allowed():

    user = User(is_admin=True)

    result = is_user_allowed(user)

    assert result is True