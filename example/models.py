from django.db import models

class Book(models.Model):
    bid = models.IntegerField(primary_key=True)
    day = models.CharField(max_length=50)

