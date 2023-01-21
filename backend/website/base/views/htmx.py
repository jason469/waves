from django.http.response import HttpResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth import get_user_model


@require_http_methods(['POST'])
def check_username(request):
    username = request.POST.get('username')

    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("This username already exists")

    return HttpResponse()
