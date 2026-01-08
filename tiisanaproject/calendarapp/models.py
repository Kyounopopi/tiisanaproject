from django.db import models

# Create your models here.

from django.db import models

class DailyRecord(models.Model):
    date = models.DateField()
    image = models.ImageField(upload_to="photos/")
    comment = models.TextField(blank=True)

    def __str__(self):
        return str(self.date)
