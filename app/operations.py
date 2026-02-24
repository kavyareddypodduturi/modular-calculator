from abc import ABC, abstractmethod
from app.exceptions import DivisionByZeroError


class Operation(ABC):
    """Strategy interface for calculator operations."""

    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        pass  # pragma: no cover


class Add(Operation):
    def execute(self, a, b):
        return a + b


class Subtract(Operation):
    def execute(self, a, b):
        return a - b


class Multiply(Operation):
    def execute(self, a, b):
        return a * b


class Divide(Operation):
    def execute(self, a, b):
        if b == 0:
            raise DivisionByZeroError("Cannot divide by zero")
        return a / b


class Power(Operation):
    def execute(self, a, b):
        return a ** b


class Root(Operation):
    def execute(self, a, b):
        return a ** (1 / b)