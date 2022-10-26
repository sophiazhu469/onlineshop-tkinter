# throw this error when failed to pass validation, e.g. invalid customer name

class BadRequestError(Exception):
    def __init__(self, message='Invalid request'):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message