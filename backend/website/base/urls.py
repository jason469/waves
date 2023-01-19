from django.urls import path
from backend.website.base.views import views, htmx
from django.contrib.auth.views import LogoutView

app_name = 'website__base'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("register/", views.RegisterView.as_view(), name="register")
]

htmx_urlpatterns = [
    path('check-username/', htmx.check_username, name='check-username')
]

urlpatterns += htmx_urlpatterns