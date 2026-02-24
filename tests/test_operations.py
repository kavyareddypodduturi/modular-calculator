import pytest
from app.operations import Add, Subtract, Multiply, Divide, Power, Root
from app.exceptions import DivisionByZeroError


@pytest.mark.parametrize(
    "operation,a,b,expected",
    [
        (Add(), 2, 3, 5),
        (Subtract(), 5, 3, 2),
        (Multiply(), 4, 3, 12),
        (Divide(), 10, 2, 5),
        (Power(), 2, 3, 8),
        (Root(), 9, 2, 3),
    ],
)
def test_operations(operation, a, b, expected):
    assert operation.execute(a, b) == expected


def test_divide_by_zero():
    with pytest.raises(DivisionByZeroError):
        Divide().execute(10, 0)