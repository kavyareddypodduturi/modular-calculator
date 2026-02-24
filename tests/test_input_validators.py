import pytest
from app.input_validators import validate_numbers
from app.exceptions import InvalidInputError


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ("2", "3", (2.0, 3.0)),
        ("5.5", "2", (5.5, 2.0)),
        ("-1", "4", (-1.0, 4.0)),
    ],
)
def test_validate_numbers_valid(a, b, expected):
    assert validate_numbers(a, b) == expected


@pytest.mark.parametrize(
    "a,b",
    [
        ("", "2"),
        ("a", "3"),
        ("2", "b"),
    ],
)
def test_validate_numbers_invalid(a, b):
    with pytest.raises(InvalidInputError):
        validate_numbers(a, b)