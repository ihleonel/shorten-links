from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request


@api_view(['GET'])
def shorter_url(request: Request) -> Response:
    query_params: dict = request.query_params.dict()
    print(query_params)

    data = {'url': f" modified {query_params['link']}"}
    headers = {
        'Access-Control-Allow-Origin': '*'
    }
    return Response(data=data, headers=headers)
