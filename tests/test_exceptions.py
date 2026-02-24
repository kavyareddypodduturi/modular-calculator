import pytest
from app.exceptions import (
    CalculatorError,
    DivisionByZeroError,
    InvalidInputError,
    InvalidOperationError,
)


def test_exception_inheritance():
    assert issubclass(DivisionByZeroError, CalculatorError)
    assert issubclass(InvalidInputError, CalculatorError)
    assert issubclass(InvalidOperationError, CalculatorError)


def test_raise_exceptions():
    with pytest.raises(DivisionByZeroError):
        raise DivisionByZeroError("division error")

    with pytest.raises(InvalidInputError):
        raise InvalidInputError("input error")

    with pytest.raises(InvalidOperationError):
        raise InvalidOperationError("operation error")