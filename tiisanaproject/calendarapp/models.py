# models.py
from django.db import models

class CalendarDay(models.Model):
    date = models.DateField(unique=True)

    def __str__(self):
        return str(self.date)


class DayEntry(models.Model):
    day = models.ForeignKey(
        CalendarDay,
        related_name='entries',
        on_delete=models.CASCADE
    )
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    comment = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
