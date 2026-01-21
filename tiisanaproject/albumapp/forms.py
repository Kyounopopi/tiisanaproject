from django import forms
from .models import Album

class AlbumCreateForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ["name"]


class PhotoUploadForm(forms.Form):
    images = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
        required=False
    )
    
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleImageField(forms.ImageField):
    widget = MultipleFileInput


class PhotoUploadForm(forms.Form):
    images = MultipleImageField(required=False)
