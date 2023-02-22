from django import forms


class AllSearchForm(forms.Form):
    required_css_class = 'required'

    SEARCH_CHOICES = (
        ("song", "Song"),
        ("artist", "Artist"),
        ("playlist", "Playlist"),
    )

    value = forms.CharField(
        required=True,
        label="Search",
        widget=forms.TextInput(attrs={'placeholder': 'What are you looking for?'})
    )

    type = forms.ChoiceField(
        required=True,
        label="What are you searching for?",
        choices=SEARCH_CHOICES,
        widget=forms.Select(attrs={'id': 'searchChoices'})
    )
