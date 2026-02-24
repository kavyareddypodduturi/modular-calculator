import pandas as pd


class Observer:
    """Base observer class."""

    def update(self, data):
        pass  # pragma: no cover


class AutoSaveObserver(Observer):
    """Automatically saves history when updated."""

    def __init__(self, history):
        self.history = history

    def update(self, data):
        self.history.save()


class History:
    """Manages calculation history using pandas."""

    def __init__(self, file_path="history.csv"):
        self.file_path = file_path
        self.df = pd.DataFrame(columns=["operation", "a", "b", "result"])
        self.observers = []
        self.load()

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self.df)

    def add(self, operation, a, b, result):
        new_row = {
            "operation": operation,
            "a": a,
            "b": b,
            "result": result,
        }
        self.df = pd.concat([self.df, pd.DataFrame([new_row])], ignore_index=True)
        self.notify()

    def save(self):
        self.df.to_csv(self.file_path, index=False)

    def load(self):
        try:
            self.df = pd.read_csv(self.file_path)
        except FileNotFoundError:
            pass  # pragma: no cover

    def clear(self):
        self.df = pd.DataFrame(columns=["operation", "a", "b", "result"])

    def show(self):
        return self.df