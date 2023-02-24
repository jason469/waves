import datetime
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
        Playlist.objects.create(
            user=form,
            name="Favourites"
        )
        return super().form_valid(form)


class Logout(LogoutView):
    success_url = reverse_lazy('website__base:login')


def index(request):
    current_user = request.user
    all_playlists = list(Playlist.objects.filter(user=current_user))
    if (len(all_playlists) > 6):
        random_playlists = random.sample(all_playlists, 6)
    else:
        random_playlists = all_playlists

    current_hour = datetime.datetime.now().hour
    if 0 <= current_hour < 12:
        header = "Good Morning"
    elif 12 <= current_hour <= 18:
        header = "Good Afternoon"
    else:
        header = "Good Evening"

    print(datetime.datetime.now().hour)

    context = {
        "random_playlists": random_playlists,
        "header": header
    }
    return render(request, 'base/pages/index.html', context=context)


def profile(request):
    user = request.user
    number_of_playlists = Playlist.objects.filter(user=user).distinct().count()
    context = {
        "user": user,
        "number_of_playlists": number_of_playlists
    }
    return render(request, 'base/pages/profile.html', context=context)
