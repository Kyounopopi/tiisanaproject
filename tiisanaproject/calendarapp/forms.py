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
        fields = ['image', 'comment']  # imageとcommentの両方を含める
        widgets = {
            'comment': forms.Textarea(attrs={
                'placeholder': 'コメントを入力',
                'rows': 4
            }),
        }

class DailyRecordForm(forms.ModelForm):
    class Meta:
        model = DailyRecord
        fields = ['image', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={
                'placeholder': 'コメントを書く',
                'rows': 3
            }),
        }
