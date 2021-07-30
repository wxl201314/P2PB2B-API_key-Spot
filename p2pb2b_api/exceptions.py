
class P2pb2bError(Exception):
    ''' '''

    def __init__(self, message: str, status_code: int, error_code: int=None):
        self.message = message
        self.status_code = status_code
        self.error_code = error_code

    def __str__(self):
        return (f'\n\tMessage: {self.message}' +
                f'\n\tHTTP status code: {self.status_code}' +
                (f'\n\tP2pb2b error code: {self.error_code}'
                    if self.error_code else ''))

class NotFound(P2pb2bError):

    def __init__(self, method: str):
        self.method = method
        super().__init__(f'wrong method "{self.method}"', 404)
