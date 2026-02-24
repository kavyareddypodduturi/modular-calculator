from app.operations import Add, Subtract, Multiply, Divide, Power, Root
from app.exceptions import InvalidOperationError


class OperationFactory:
    """Factory to create operation instances."""

    operations = {
        "add": Add,
        "subtract": Subtract,
        "multiply": Multiply,
        "divide": Divide,
        "power": Power,
        "root": Root,
    }

    @classmethod
    def create_operation(cls, operation_name: str):
        operation_class = cls.operations.get(operation_name.lower())
        if not operation_class:
            raise InvalidOperationError(f"Invalid operation: {operation_name}")
        return operation_class()


class Calculation:
    """Handles performing calculations using operations."""

    def __init__(self, operation_name: str, a: float, b: float):
        self.operation = OperationFactory.create_operation(operation_name)
        self.a = a
        self.b = b

    def perform(self):
        return self.operation.execute(self.a, self.b)