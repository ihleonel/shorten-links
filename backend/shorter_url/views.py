from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from pyshorteners import Shortener
from rest_framework import status
from .validator import Validator

@api_view(['POST'])
def shorter_url(request: Request) -> Response:

    validator = Validator(request)
    if not validator.is_valid():
        return Response({**validator.data, 'errors': {**validator.errors} }, status=status.HTTP_400_BAD_REQUEST)

    link = validator.valid['link']

    shortener = Shortener()
    shorted_link = shortener.tinyurl.short(link)

    return Response({'shorted': shorted_link}, status=status.HTTP_201_CREATED)
