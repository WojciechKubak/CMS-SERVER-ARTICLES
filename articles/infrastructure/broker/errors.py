

class ConsumerServiceError(Exception):
    def __init__(self, message='Consumer service error') -> None:
        self.message = message
        super().__init__(self.message)


class TranslationHandlerError(ConsumerServiceError):
    def __init__(self, message='Tag does not exist') -> None:
        self.message = message
        super().__init__(self.message)
