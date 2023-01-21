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
    )

    type = forms.ChoiceField(
        required=True,
        label="Type",
        choices=SEARCH_CHOICES
    )
