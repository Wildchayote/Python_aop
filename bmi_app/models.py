from django.db import models

class BMIRecord(models.Model):
    name = models.CharField(max_length=120)
    height = models.FloatField(blank=False, null=True)
    weight = models.FloatField(blank=False, null=True)
    BMI = models.FloatField(blank=False, null=True)
    date = models.DateTimeField(auto_now_add=True)
