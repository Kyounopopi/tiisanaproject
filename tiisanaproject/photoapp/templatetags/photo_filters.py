import os
from django import template

register = template.Library()

@register.filter
def basename(value):
    """ファイルパスからファイル名のみを取得"""
    return os.path.basename(value)