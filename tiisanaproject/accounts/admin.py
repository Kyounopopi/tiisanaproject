from django.contrib import admin

from .models import Customuser
from .models import Account


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')
    list_display_links = ('id', 'username')


class AccountAdmin(admin.ModelAdmin):
    """
    Accountプロフィールの管理画面設定
    """
    list_display = (
        'id',
        'get_username',
        'gender',
        'birth_date',
        'get_age',
        'has_profile_image',
        'icon_color'
    )
    list_display_links = ('id', 'get_username')
    search_fields = ('user__username', 'user__email')
    list_filter = ('gender',)
    readonly_fields = ('get_age',)
    
    # fieldsetsからcreated_atとupdated_atを完全に削除
    fieldsets = (
        ('ユーザー情報', {
            'fields': ('user',)
        }),
        ('プロフィール情報', {
            'fields': ('gender', 'birth_date', 'profile_image', 'icon_color')
        }),
    )
    
    def get_username(self, obj):
        """ユーザー名を表示"""
        return obj.user.username
    get_username.short_description = 'ユーザー名'
    get_username.admin_order_field = 'user__username'
    
    def has_profile_image(self, obj):
        """プロフィール画像の有無"""
        return bool(obj.profile_image)
    has_profile_image.short_description = '画像'
    has_profile_image.boolean = True
    
    def get_age(self, obj):
        """年齢を表示"""
        age = obj.get_age()
        return f"{age}歳" if age else "未設定"
    get_age.short_description = '年齢'


# モデルを登録
admin.site.register(Customuser, CustomUserAdmin)
admin.site.register(Account, AccountAdmin)

# 管理サイトのカスタマイズ
admin.site.site_header = 'アカウント管理システム'
admin.site.site_title = '管理サイト'
admin.site.index_title = 'ダッシュボード'