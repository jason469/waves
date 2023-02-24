import random

from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import FormView

from backend.website.base.forms import RegisterForm
from backend.website.base.models import Playlist


class Login(LoginView):
    template_name = 'registration/login.html'


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('website__base:login')

    def form_valid(self, form):
        form.save()  # save the user
        return super().form_valid(form)


class Logout(LogoutView):
    success_url = reverse_lazy('website__base:login')


def index(request):
    all_playlists = list(Playlist.objects.all())

    # change 3 to how many random items you want
    random_playlists = random.sample(all_playlists, 6)
    context = {
        "random_playlists": random_playlists
    }
    return render(request, 'base/pages/index.html', context=context)


def profile(request):
    user = request.user
    number_of_playlists =  Playlist.objects.filter(user=user).distinct().count()
    context = {
        "user": user,
        "number_of_playlists": number_of_playlists
    }
    return render(request, 'base/pages/profile.html', context=context)
