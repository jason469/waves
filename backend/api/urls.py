from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from backend.api.views.base import UserView

app_name = 'api'

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),

    path('user/', UserView.as_view(), name='api__user'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
