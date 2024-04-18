from django.http import JsonResponse


def index(request):
    return JsonResponse({'messaje': 'Hello, world'})
