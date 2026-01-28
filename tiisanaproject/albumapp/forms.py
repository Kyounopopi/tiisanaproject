from django import forms
from .models import Album


class AlbumCreateForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ["name"]


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class PhotoCreateForm(forms.Form):
    images = forms.FileField(
        widget=MultipleFileInput(attrs={"multiple": True}),
        required=True
    )
