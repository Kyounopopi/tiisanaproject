from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    """写真のカテゴリ"""
    name = models.CharField(max_length=100, unique=True, verbose_name="カテゴリ名")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")

    class Meta:
        verbose_name = "カテゴリ"
        verbose_name_plural = "カテゴリ"

    def __str__(self):
        return self.name


class Tag(models.Model):
    """写真のタグ"""
    name = models.CharField(max_length=50, unique=True, verbose_name="タグ名")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")

    class Meta:
        verbose_name = "タグ"
        verbose_name_plural = "タグ"

    def __str__(self):
        return self.name


class Photo(models.Model):
    # 基本情報
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name="画像")
    title = models.CharField(max_length=200, blank=True, verbose_name="タイトル")
    description = models.TextField(blank=True, verbose_name="説明")
    
    # 関連情報
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='photos',
        verbose_name="カテゴリ"
    )
    tags = models.ManyToManyField(
        Tag, 
        blank=True,
        related_name='photos',
        verbose_name="タグ"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='photos',
        verbose_name="投稿者"
    )
    
    # 日時情報
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")
    taken_at = models.DateTimeField(null=True, blank=True, verbose_name="撮影日時")

    class Meta:
        verbose_name = "写真"
        verbose_name_plural = "写真"
        ordering = ['-created_at']

    def __str__(self):
        return self.title if self.title else f"Photo {self.id}"