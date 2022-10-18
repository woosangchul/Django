from django.db import models
from django.contrib.auth.models import User

class Routine(models.Model):
    routine_id = models.AutoField(primary_key=True)
    account_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    category = models.CharField(max_length=128)
    goal = models.TextField()
    is_alarm = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

