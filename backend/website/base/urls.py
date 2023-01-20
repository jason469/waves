from django.contrib.auth.decorators import login_required
from django.urls import path
from backend.website.base.views import views, htmx

app_name = 'website__base'

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path("register/", views.RegisterView.as_view(), name="register"),

    path('', login_required(views.index), name='index'),
    path('profile/', login_required(views.profile), name='profile'),
]

htmx_urlpatterns = [
    path('check-username/', login_required(htmx.check_username), name='check-username')
]

urlpatterns += htmx_urlpatterns
