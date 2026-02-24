
# Enhanced Calculator Application with Advanced Design Patterns and Pandas

## Project Overview

This project is an advanced command-line calculator application built in Python as part of the Module 5 assignment.

It demonstrates:

* Object-Oriented Programming (OOP)
* Advanced Design Patterns (Factory, Strategy, Observer, Memento, Facade)
* Data management using pandas
* Persistent CSV-based history
* Structured error handling (LBYL and EAFP)
* Automated testing using pytest
* 100% test coverage enforcement
* Continuous Integration using GitHub Actions

The application runs in a REPL (Read–Eval–Print Loop) environment and supports undo/redo functionality along with persistent calculation history.

---

## Features

### Supported Operations

* Addition (`add`)
* Subtraction (`subtract`)
* Multiplication (`multiply`)
* Division (`divide`)
* Power (`power`)
* Root (`root`)

---

### Available Commands

* `help` → Display usage instructions
* `history` → Show calculation history
* `clear` → Clear calculation history
* `undo` → Undo last calculation
* `redo` → Redo last undone calculation
* `save` → Save history to CSV
* `load` → Load history from CSV
* `exit` → Close the application

---

## Design Patterns Implemented

### Factory Pattern

The `OperationFactory` dynamically creates operation objects based on user input.

### Strategy Pattern

Each arithmetic operation is implemented as a separate strategy class with a common execution interface.

### Observer Pattern

`AutoSaveObserver` automatically saves calculation history when auto-save is enabled.

### Memento Pattern

The `Caretaker` class stores snapshots of history state to support undo and redo functionality.

### Facade Pattern

The `Calculator` class provides a simplified interface that coordinates calculations, validation, history management, and state control.

---

## Data Management with pandas

* Calculation history is stored in a pandas `DataFrame`.
* History is persisted as a CSV file.
* History auto-loads when the application starts.
* Column integrity is maintained when loading CSV files.
* Data is displayed in structured tabular format.

---

## Error Handling

The project demonstrates both:

### LBYL (Look Before You Leap)

* Prevents division by zero.
* Prevents invalid root operations.
* Validates operation names before execution.

### EAFP (Easier to Ask Forgiveness than Permission)

* Handles invalid numeric inputs.
* Handles configuration errors.
* Handles file loading failures gracefully.
* Uses custom exception classes for calculator-specific errors.

---

## Project Structure

```
modular-calculator/
├── app/
│   ├── __init__.py
│   ├── calculation.py
│   ├── calculator_config.py
│   ├── calculator_memento.py
│   ├── calculator_repl.py
│   ├── exceptions.py
│   ├── history.py
│   ├── input_validators.py
│   └── operations.py
├── tests/
│   ├── test_calculations.py
│   ├── test_calculator_config.py
│   ├── test_calculator_memento.py
│   ├── test_calculator_repl.py
│   ├── test_exceptions.py
│   ├── test_history.py
│   ├── test_input_validators.py
│   └── test_operations.py
├── .github/workflows/python-app.yml
├── .coveragerc
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### 1. Create Virtual Environment

```
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

---

## Running the Application

```
python -m app.calculator_repl
```

---

## Example Usage

```
>> add 2 3
Result: 5.0

>> history
(Displays pandas table of previous calculations)

>> undo
Undo complete

>> redo
Redo complete

>> exit
```

---

## Testing

### Run Tests

```
pytest
```

### Run with Coverage

```
export PYTHONPATH=.
pytest --cov=app --cov-branch
coverage report --fail-under=100
```

### Coverage Requirement

The project enforces:

* 100% line coverage
* 100% branch coverage

---

## Continuous Integration

GitHub Actions automatically:

* Installs dependencies
* Runs all tests
* Measures coverage
* Enforces 100% coverage
* Fails the build if coverage drops below threshold

Workflow file location:

```
.github/workflows/python-app.yml
```

---

## Technologies Used

* Python
* pandas
* pytest
* pytest-cov
* python-dotenv
* Git
* GitHub
* GitHub Actions

---

## Academic Use

This project is developed for academic purposes as part of coursework.
