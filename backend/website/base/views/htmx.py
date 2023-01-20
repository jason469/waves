from django.http.response import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from django.contrib.auth import get_user_model

from backend.website.base.forms import RegisterForm


def check_username(request):
    username = request.POST.get('username')

    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("This username already exists")

    return HttpResponse()
