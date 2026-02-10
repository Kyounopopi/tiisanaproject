from django import forms
from .models import Album


class AlbumCreateForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ["name"]


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class PhotoCreateForm(forms.Form):

    existing_images = forms.MultipleChoiceField(
        required = False,
        widget=forms.CheckboxSelectMultiple
    )

    def __init__(self, *args, **kwargs):
        image_choices = kwargs.pop("image_choices",[])
        super().__init__(*args,**kwargs)

        self.fields["existing_images"].choices = image_choices

    def clean_images(self):
        cleaned_data = super().clean()

        cleaned_data["images"] = self.files.getlist("images")

        return cleaned_data

       
