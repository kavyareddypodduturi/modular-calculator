from app.calculator_memento import Caretaker


def test_undo_redo():
    caretaker = Caretaker()

    state1 = {"value": 1}
    state2 = {"value": 2}

    caretaker.save(state1)
    caretaker.save(state2)

    undo_state = caretaker.undo()
    assert undo_state == state1  # previous state

    redo_state = caretaker.redo()
    assert redo_state == state2  # next state


def test_undo_empty():
    caretaker = Caretaker()
    assert caretaker.undo() is None


def test_redo_empty():
    caretaker = Caretaker()
    assert caretaker.redo() is None

def test_save_drops_future_states():
    caretaker = Caretaker()
    caretaker.save({"v": 0})
    caretaker.save({"v": 1})
    caretaker.undo()          # now current is v=0, future exists
    caretaker.save({"v": 99}) # should drop future
    assert caretaker.redo() is None    