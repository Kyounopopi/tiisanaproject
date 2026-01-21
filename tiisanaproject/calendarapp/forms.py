from django import forms
from .models import DayEntry
from .models import DailyRecord

class DayEntryForm(forms.ModelForm):
    class Meta:
        model = DayEntry
        fields = ['photo', 'comment']

class CommentForm(forms.ModelForm):
    class Meta:
        model = DailyRecord
        fields = ["comment"]
        widgets = {
            "comment": forms.Textarea(attrs={
                "rows": 3,
                "class": "comment-textarea",
                "placeholder": "コメントを入力"
            })
        }

class DailyRecordForm(forms.ModelForm):
    class Meta:
        model = DailyRecord
        fields = ['image', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'コメントを書く'
            })
        }
