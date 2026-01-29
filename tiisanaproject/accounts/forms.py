from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Account,UserProfile

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    """
    基本的なユーザー登録フォーム（Customuser用）
    """
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class AccountRegistrationForm(UserCreationForm):
    """
    Customuser + Account プロフィール同時登録フォーム
    """
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'メールアドレス'
        })
    )

    first_name = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '名'
        })
    )

    last_name = forms.CharField(
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '姓'
        })
    )

    gender = forms.ChoiceField(
        choices=Account.GENDER_CHOICES,
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

    birth_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )

    icon_color = forms.CharField(
        max_length=7,
        required=False,
        initial='#667eea',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'color',
            'placeholder': '#667eea'
        }),
        help_text='プロフィール画像未設定時のアイコン背景色'
    )

    class Meta:
        model = User
        fields = [
            'username', 'email', 'first_name', 'last_name',
            'password1', 'password2'
        ]
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ユーザー名'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'パスワード'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'パスワード（確認）'
        })

    def save(self, commit=True):
        # Customuserを保存
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            # Accountプロフィールを作成
            Account.objects.create(
                user=user,
                gender=self.cleaned_data.get('gender', 'not_specified'),
                birth_date=self.cleaned_data.get('birth_date'),
                icon_color=self.cleaned_data.get('icon_color', '#667eea')
            )
        return user


class AccountUpdateForm(forms.ModelForm):
    """
    Accountプロフィール更新フォーム
    """
    class Meta:
        model = Account
        fields = [
            'gender', 'birth_date', 'profile_image', 'icon_color'
        ]
        widgets = {
            'gender': forms.Select(attrs={
                'class': 'form-control'
            }),
            'birth_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'profile_image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
            'icon_color': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'color'
            })
        }



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['display_name','gender','birth_date','icon_color','profile_image']
        widgets = {
            'display_name': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'表示名'
            }),
            'gender': forms.Select(attrs={'class':'form-control'}),
            'birth_date': forms.DateInput(attrs={
                'type':'date',
                'class':'form-control'
            }),
            'icon_color': forms.TextInput(attrs={
                'type': 'color',
                'class':'form-control'
            }),
            'profile_image': forms.FileInput(attrs={
                'class':'form-control'
            }),
        }


 