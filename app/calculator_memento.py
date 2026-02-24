class CalculatorMemento:
    """Stores calculator state."""
    def __init__(self, state):
        self.state = state


class Caretaker:
    """Undo/Redo manager using a current pointer (reliable)."""

    def __init__(self):
        self._states = []
        self._index = -1  # points to current state

    def save(self, state):
        # If we undo and then do a new action, drop "future" states
        if self._index < len(self._states) - 1:
            self._states = self._states[: self._index + 1]

        self._states.append(CalculatorMemento(state))
        self._index += 1

    def undo(self):
        if self._index <= 0:
            return None
        self._index -= 1
        return self._states[self._index].state

    def redo(self):
        if self._index >= len(self._states) - 1:
            return None
        self._index += 1
        return self._states[self._index].state