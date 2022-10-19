from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    bid = models.IntegerField()
    day = models.CharField(max_length=50)

