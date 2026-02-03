from django.contrib import admin
from .models import Photo, Category, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']
    ordering = ['name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']
    ordering = ['name']


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'category', 'created_at', 'image_thumbnail']
    list_filter = ['category', 'tags', 'created_at']
    search_fields = ['title', 'description', 'user__username']
    filter_horizontal = ['tags']
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    
    fieldsets = (
        ('基本情報', {
            'fields': ('image', 'title', 'description', 'user')
        }),
        ('分類', {
            'fields': ('category', 'tags')
        }),
        ('日時情報', {
            'fields': ('taken_at', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at']
    
    def image_thumbnail(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="50" height="50" style="object-fit: cover; border-radius: 4px;" />'
        return '-'
    image_thumbnail.short_description = 'サムネイル'
    image_thumbnail.allow_tags = True