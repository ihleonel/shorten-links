from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from rest_framework import status
from .validator import Validator
from .service import Service

@api_view(['POST'])
def shorter_url(request: Request) -> Response:

    validator = Validator(request)
    if not validator.is_valid():
        return Response({**validator.data, 'errors': {**validator.errors} }, status=status.HTTP_400_BAD_REQUEST)

    service = Service()
    shorted_link = service(validator.valid)

    return Response({'shorted': shorted_link}, status=status.HTTP_201_CREATED)
