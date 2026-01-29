from django.db import models

from django.contrib.auth.models import AbstractUser
from datetime import date

class Customuser(AbstractUser):
    pass


class Account(models.Model):
    """
    拡張ユーザーモデル(プロフィール情報付き)
    """

    user = models.OneToOneField(
        Customuser,
        on_delete=models.CASCADE,
        related_name='account_profile',
        verbose_name='ユーザー'
    )
    GENDER_CHOICES = [
        ('male','男性'),
        ('female','女性'),
        ('other','その他'),
        ('not_specified','未設定'),
    ]

    #性別

    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES,
        default='not_specified',
        verbose_name='性別'
    )

    birth_date = models.DateField(
        blank=True,
        null=True,
        verbose_name='生年月日'
    )

    profile_image = models.ImageField(
        upload_to='profile_images/',
        blank=True,
        null=True,
        verbose_name='プロフィール画像'
    )

    icon_color = models.CharField(
        max_length=7,
        default='#667eea',
        blank=True,
        verbose_name='アイコンカラー',
        help_text='画像未設定時のアイコン背景色'
    )

    class Meta:
        verbose_name = 'アカウント'
        verbose_name_plural = 'アカウント'

    def __str__(self):
        return f"{self.user.username}のプロフィール"
    
    def get_user_info(self):
        """ユーザー情報を辞書形式で取得"""
        return{
            'id':self.id,
            'username':self.username,
            'email':self.email,
            'gender':self.get_gender_display(),
            'birth_date':self.birth_date,
            'age':self.get_age(),
            'icon_url':self.get_icon_url(),
        }
    
    def get_age(self):
        """年齢を計算して取得"""
        if not self.birth_date:
            return None
        
        today = date.today()
        age = today.year - self.birth_date.year

        if(today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age

    def get_icon_url(self):
        """アイコン画像のURLを取得"""
        if self.profile_image:
            return self.profile_image.url
        else:
            return '/static/images/default_icon.png'
        
    def get_gender_japanese(self):
        """性別を日本語で取得"""
        return self.get_gender_display()

class User(models.Model):
    # アカウントアイコン
    user = models.OneToOneField(
        Customuser,
        on_delete=models.CASCADE,
        related_name='アイコン'
    )

    GENDER_CHOICES = [
        ('male','男性'),
        ('female','女性'),
        ('other','その他'),
        ('not_specified','未設定'),
    ]


    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES,
        default='not_specified',
        verbose_name='生年月日'
    )



    birth_date = models.DateField(
        blank=True,
        null=True,
        verbose_name='生年月日'
    )

    icon = models.ImageField(
        upload_to='user_icons/',
        blank=True,
        null=True,
        verbose_name='アイコン画像'
    ) 


    def get_user_info(self):
        return{
            'id':self.id,
            'username':self.user.username,
            'email':self.user.email,
            'gender':self.get_gender_display(),
            'birth_date':self.birth_date,
            'age':self.get_age(),
        }
    
    def get_age(self):
        if not self.birth_date:
            return None
        
        today = date.today()
        age = today.year -self.birth_date.year

        if(today.month, today.day)< (self.birth_date.month,self.birth_date.day):
            age -= 1

        return age
    
    def get_icon_url(self):
        if self.icon:
            return self.icon.url
        else:
            return '/static/images/default_icon.png'

    def get_gender_japanese(self):
        return self.get_gender_display()

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'ユーザー'
        verbose_name_plural = 'ユーザー'