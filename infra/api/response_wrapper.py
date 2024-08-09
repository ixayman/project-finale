class ResponseWrapper:

    def __init__(self, ok, status, data):
        self._ok = ok
        self._status = status
        self._data = data

    @property
    def ok(self):
        return self._ok

    @property
    def status_code(self):
        return self._status

    @property
    def data(self):
        return self._data


