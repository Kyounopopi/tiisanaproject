from django import forms
from .models import Photo, Category, Tag


class PhotoForm(forms.ModelForm):
    # タグを複数選択可能にする
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label="タグ"
    )
    
    # 新しいタグを追加できるフィールド
    new_tags = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'カンマ区切りで新しいタグを追加 (例: 風景, 家族, 旅行)',
            'class': 'form-control'
        }),
        label="新しいタグを追加"
    )

    class Meta:
        model = Photo
        fields = ['image', 'title', 'description', 'category', 'tags', 'taken_at']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '写真のタイトルを入力'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': '写真の説明を入力'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
            'taken_at': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
        }
        labels = {
            'image': '画像',
            'title': 'タイトル',
            'description': '説明',
            'category': 'カテゴリ',
            'taken_at': '撮影日時'
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        
        # 新しいタグの処理
        new_tags = self.cleaned_data.get('new_tags', '')
        if new_tags:
            tag_names = [name.strip() for name in new_tags.split(',') if name.strip()]
            for tag_name in tag_names:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                instance.tags.add(tag)
        
        if commit:
            instance.save()
            self.save_m2m()  # 多対多の関係を保存
        
        return instance


class PhotoSearchForm(forms.Form):
    search = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'タイトル、説明、タグで検索',
            'class': 'form-control'
        }),
        label="検索"
    )
    
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        empty_label="すべてのカテゴリ",
        widget=forms.Select(attrs={
            'class': 'form-control'
        }),
        label="カテゴリ"
    )
    
    tag = forms.ModelChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        empty_label="すべてのタグ",
        widget=forms.Select(attrs={
            'class': 'form-control'
        }),
        label="タグ"
    )
    
    date_from = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        }),
        label="日付（開始）"
    )
    
    date_to = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        }),
        label="日付（終了）"
    )
    
    SORT_CHOICES = [
        ('-created_at', '新しい順'),
        ('created_at', '古い順'),
        ('title', 'タイトル順'),
        ('-taken_at', '撮影日時（新しい順）'),
        ('taken_at', '撮影日時（古い順）'),
    ]
    
    sort = forms.ChoiceField(
        choices=SORT_CHOICES,
        required=False,
        initial='-created_at',
        widget=forms.Select(attrs={
            'class': 'form-control'
        }),
        label="並び替え"
    )