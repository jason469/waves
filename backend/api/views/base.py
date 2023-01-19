from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.api.serializers.base import UserSerializer


class UserView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = User.objects.all()
        serializer = UserSerializer
        return Response(serializer.data)
