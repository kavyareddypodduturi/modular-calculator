import os
from app.calculator_repl import Calculator


def test_calculator_add():
    calc = Calculator("test_history.csv")
    result = calc.calculate("add", "2", "3")
    assert result == 5


def test_calculator_history():
    calc = Calculator("test_history.csv")
    calc.calculate("add", "1", "2")

    history = calc.show_history()
    assert not history.empty


def test_calculator_clear():
    calc = Calculator("test_history.csv")
    calc.calculate("add", "1", "2")
    calc.clear_history()

    assert calc.show_history().empty


def test_calculator_undo_redo():
    file_name = "test_history.csv"

    # Remove old file if exists
    if os.path.exists(file_name):
        os.remove(file_name)

    calc = Calculator(file_name, enable_autosave=False)

    calc.calculate("add", "1", "2")
    calc.calculate("multiply", "2", "3")

    calc.undo()
    assert len(calc.show_history()) == 1

    calc.redo()
    assert len(calc.show_history()) == 2

    # Cleanup after test
    if os.path.exists(file_name):
        os.remove(file_name)