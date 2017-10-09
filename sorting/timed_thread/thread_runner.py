from .timed_thread import TimedThread

class ThreadRunner(object):
    def __init__(self, func, data):
        self._data = data
        self._func = func

    def run_in_thread(self):
        thread = TimedThread(target=self._func, data=self._data)
        thread.run_process()
        return thread