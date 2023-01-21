from django import forms


class AddPlaylistForm(forms.Form):
    required_css_class = 'required'

    name = forms.CharField(
        required=True,
        label="Name",
        help_text="Name of the playlist"
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 2, "cols": 30}),
        required=False,
        label="Description",
        help_text="Description of the playlist"
    )
