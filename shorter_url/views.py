from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from pyshorteners import Shortener


@api_view(['POST'])
def shorter_url(request: Request) -> Response:

    link: str = request.data.get('link')

    shortener = Shortener()
    shorted_link = shortener.tinyurl.short(link)
    data: dict = {'shorted': shorted_link}

    return Response(data=data)
