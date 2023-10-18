from django.db import models

class Nation(models.Model):
    nation = models.CharField(max_length=120)
    capital = models.CharField(max_length=120)
    date = models.DateTimeField(auto_now_add=True)
