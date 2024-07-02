from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from pyshorteners import Shortener
from rest_framework.status import HTTP_400_BAD_REQUEST
from .validator import Validator

@api_view(['POST'])
def shorter_url(request: Request) -> Response:
    print('request link !!!')
    validator = Validator(request)
    if not validator.is_valid():
        return Response(validator.errors, status=HTTP_400_BAD_REQUEST)

    link = validator.data

    shortener = Shortener()
    shorted_link = shortener.tinyurl.short(link)
    data: dict = {'shorted': shorted_link}

    return Response(data=data)
