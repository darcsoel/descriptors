#  pylint:disable=missing-module-docstring
#  pylint:disable=missing-function-docstring

"""
Unit tests
"""

import pytest

from main import Demo


def test_valid_value() -> None:
    dummy = Demo(2)
    assert dummy.field == 2
    assert dummy.other is None


def test_str_value() -> None:
    with pytest.raises(ValueError):
        Demo("2")  # type: ignore
