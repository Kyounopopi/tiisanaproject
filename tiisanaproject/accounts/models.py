from django.db import models

from django.contrib.auth.models import AbstractUser
from datetime import date

class Customuser(AbstractUser):
    pass


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


    def get_user_info(self):
        return{
            'id':self.id,
            'username':self.username,
            'email':self.email,
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
        return self.username
    
    class Meta:
        verbose_name = 'ユーザー'
        verbose_name_plural = 'ユーザー'