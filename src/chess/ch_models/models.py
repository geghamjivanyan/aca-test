from django.db import models

# Create your models here.

class Bank(models.Model):
    name = models.CharField(max_length=30)
    branch_count = models.PositiveSmallIntegerField(default=0)
    usd_buy = models.FloatField()
    usd_sell = models.FloatField()
    euro_buy = models.FloatField()
    euro_sell = models.FloatField()

    def __str__(self):
        return self.name

