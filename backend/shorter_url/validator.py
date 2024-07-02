from rest_framework.request import Request

class Validator():
    data = None
    errors = []

    def __init__(self, request: Request) -> None:
        self.request = request

    def is_valid(self) -> bool:
        self.data = self.request.data.get('link', None)
        if self.data is None:
            self.errors.append('Link is required')
        elif self.data.strip() == '':
            self.errors.append('Link is not valid')

        return len(self.errors) == 0

