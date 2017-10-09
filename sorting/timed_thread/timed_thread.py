import multiprocessing
import time
from multiprocessing import Manager

class TimedThread(object):
    def __init__(self, target, data):
        self._target = target
        self._data = data
        self._timeout = 30
        self._terminated = False

    def get_time_alotted(self):
        if self._terminated:
            return "process timeout"
        return self._time_alotted

    def get_thread_result(self):
        return self._thread_result

    def run_process(self):
        manager = Manager()
        return_data = manager.dict()
        process = multiprocessing.Process(target=self._target, args=(self._data, return_data))
        self._mark_time_start()
        process.start()
        process.join(self._timeout)
        terminated = self._terminate_if_alive(process)
        if terminated:
            self._terminated = True
        self._mark_time_alotted()
        self._set_thread_result(return_data)

    def _set_thread_result(self, return_data):
        if self._terminated:
            self._thread_result = "Process timeout"
        else:
            self._thread_result = return_data['result']

    def _terminate_if_alive(self, process):
        if process.is_alive():
            process.terminate()
            return True
        return False

    def _mark_time_start(self):
        self._time_started = time.time()

    def _mark_time_alotted(self):
        self._time_alotted = time.time() - self._time_started