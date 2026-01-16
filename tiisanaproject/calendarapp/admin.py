# admin.py
from django.contrib import admin
from .models import CalendarDay, DayEntry

class DayEntryInline(admin.TabularInline):
    model = DayEntry
    extra = 1

@admin.register(CalendarDay)
class CalendarDayAdmin(admin.ModelAdmin):
    inlines = [DayEntryInline]
