import pytest
from app.calculation import Calculation
from app.exceptions import InvalidOperationError


@pytest.mark.parametrize(
    "operation,a,b,expected",
    [
        ("add", 2, 3, 5),
        ("subtract", 5, 3, 2),
        ("multiply", 4, 2, 8),
        ("divide", 10, 2, 5),
        ("power", 2, 3, 8),
        ("root", 9, 2, 3),
    ],
)
def test_calculation(operation, a, b, expected):
    calc = Calculation(operation, a, b)
    assert calc.perform() == expected


def test_invalid_operation():
    with pytest.raises(InvalidOperationError):
        Calculation("invalid", 1, 2)