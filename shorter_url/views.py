from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request


@api_view(['POST', 'OPTIONS'])
def shorter_url(request: Request) -> Response:
    headers: dict = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
    }

    if request.method == 'OPTIONS':
        return Response(headers=headers)

    link: str = request.data.get('link')
    data: dict = {'shorted': link}

    return Response(data=data, headers=headers)
