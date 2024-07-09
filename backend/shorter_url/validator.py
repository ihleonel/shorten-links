from rest_framework.request import Request

class Validator():

    def __init__(self, request: Request) -> None:
        self.data = dict()
        self.errors = dict()
        self.valid = dict()

        self.data = request.data

    def is_valid(self) -> bool:
        if self.data.get('link', None) is None:
            self.errors['link'] = 'Link is required'
        elif self.data['link'].strip() == '':
            self.errors['link'] = 'Link is not valid'

        self.valid['link'] = self.data['link']

        return len(self.errors) == 0

