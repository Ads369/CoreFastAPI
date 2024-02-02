class DatabaseFetchError(Exception):
    def __init__(self, message, original_exception=None):
        self.message = message
        self.original_exception = original_exception
        prep = "TrackingApi: Ошибка получения данных из DB"
        if original_exception:
            super().__init__(f"{prep}:\n {message}. Ошибка: {str(original_exception)}")
        else:
            super().__init__(f"{prep}:\n {message}")

class RedisFetchError(Exception):
    def __init__(self, message, original_exception=None):
        self.message = message
        self.original_exception = original_exception
        prep = "TrackingApi: Ошибка получения данных из Redis"
        if original_exception:
            super().__init__(f"{prep}:\n {message}. Ошибка: {str(original_exception)}")
        else:
            super().__init__(f"{prep}:\n {message}")

