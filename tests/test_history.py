import os
import pandas as pd
from app.history import History


def test_history_add():
    history = History("test_history.csv")
    history.clear()

    history.add("add", 2, 3, 5)

    df = history.show()
    assert len(df) == 1
    assert df.iloc[0]["result"] == 5

    os.remove("test_history.csv") if os.path.exists("test_history.csv") else None


def test_history_save_load():
    file_name = "test_history.csv"
    history = History(file_name)
    history.clear()

    history.add("multiply", 2, 4, 8)
    history.save()

    new_history = History(file_name)
    df = new_history.show()

    assert len(df) == 1
    assert df.iloc[0]["operation"] == "multiply"

    os.remove(file_name)


def test_history_clear():
    history = History("test_history.csv")
    history.add("add", 1, 1, 2)
    history.clear()

    assert history.show().empty