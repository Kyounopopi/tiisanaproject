from django import forms
from .models import Album, Photo

class AlbumCreateForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ["name"]


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class PhotoCreateForm(forms.Form):
    images = forms.ImageField(
        widget=MultipleFileInput(),
        required=True
    )


class MultipleImageField(forms.ImageField):
    widget = MultipleFileInput


class PhotoUploadForm(forms.Form):
    images = MultipleImageField(required=False)
