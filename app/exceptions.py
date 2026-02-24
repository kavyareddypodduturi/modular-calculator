class CalculatorError(Exception):
    """Base exception for calculator errors."""
    pass


class InvalidOperationError(CalculatorError):
    """Raised when an invalid operation is requested."""
    pass


class DivisionByZeroError(CalculatorError):
    """Raised when division by zero occurs."""
    pass


class InvalidInputError(CalculatorError):
    """Raised when user input is invalid."""
    pass