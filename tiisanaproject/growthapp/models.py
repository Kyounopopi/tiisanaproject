from django.db import models

class GrowthRecord(models.Model):
    date = models.DateField(verbose_name="日付")
    height = models.FloatField(verbose_name="身長（cm）")
    weight = models.FloatField(verbose_name="体重（kg）")
    baby_log = models.TextField(max_length=150, verbose_name="発達状況")
    comment = models.TextField(blank=True, null=True, verbose_name="コメント")

    def __str__(self):
        return f"{self.date} の成長記録"

# Create your models here.