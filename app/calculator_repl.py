from app.history import AutoSaveObserver
from app.calculation import Calculation
from app.history import History
from app.calculator_memento import Caretaker
from app.input_validators import validate_numbers
from app.exceptions import CalculatorError


class Calculator:
    """Facade for calculator operations."""

    def __init__(self, history_file="history.csv", enable_autosave=True):
        self.history = History(history_file)
        if enable_autosave:
            self.history.attach(AutoSaveObserver(self.history))
        self.memento = Caretaker()
        self.memento.save(self.history.df.copy())

    def calculate(self, operation, a, b):
        a, b = validate_numbers(a, b)
        calc = Calculation(operation, a, b)
        result = calc.perform()

        self.history.add(operation, a, b, result)

        # Save NEW current state after change (correct memento usage)
        self.memento.save(self.history.df.copy())

        return result

    def undo(self):
        state = self.memento.undo()
        if state is not None:
            self.history.df = state

    def redo(self):
        state = self.memento.redo()
        if state is not None:
            self.history.df = state

    def show_history(self):
        return self.history.show()

    def clear_history(self):
        self.history.clear()

    def save_history(self):
        self.history.save()

    def load_history(self):
        self.history.load()


def repl():  # pragma: no cover
    calc = Calculator()

    print("Enhanced Calculator (type 'help' for commands)")

    while True:  # pragma: no cover
        try:
            user_input = input(">> ").strip().lower()

            if user_input == "exit":
                break

            if user_input == "help":
                print("Commands:")
                print("add/subtract/multiply/divide/power/root a b")
                print("history | clear | undo | redo | save | load | exit")
                continue

            if user_input == "history":
                print(calc.show_history())
                continue

            if user_input == "clear":
                calc.clear_history()
                print("History cleared")
                continue

            if user_input == "undo":
                calc.undo()
                print("Undo complete")
                continue

            if user_input == "redo":
                calc.redo()
                print("Redo complete")
                continue

            if user_input == "save":
                calc.save_history()
                print("History saved")
                continue

            if user_input == "load":
                calc.load_history()
                print("History loaded")
                continue

            parts = user_input.split()
            if len(parts) != 3:
                print("Invalid input. Type help.")
                continue

            op, a, b = parts
            result = calc.calculate(op, a, b)
            print("Result:", result)

        except CalculatorError as e:  # pragma: no cover
            print("Error:", e)       # pragma: no cover
        except Exception as e:        # pragma: no cover
            print("Unexpected error:", e)  # pragma: no cover


if __name__ == "__main__":  # pragma: no cover
    repl()