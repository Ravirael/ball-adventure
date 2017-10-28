from time import time

class Clock:
    def __init__(self):
        self._start_time = time()

    def restart(self):
        current_time = time()
        elapsed = current_time - self._start_time
        self._start_time = current_time
        return elapsed
