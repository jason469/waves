from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from backend.website.base.models import Playlist


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'password1': forms.TextInput(attrs={'placeholder': 'Password'}),
            'password2': forms.TextInput(attrs={'placeholder': 'Password Confirmation'}),
        }


    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        if commit:
            user.save()
        Playlist.objects.create(
            user=user,
            name="Favourites"
        )
        return user
