from django.db import models
from django.contrib.auth import get_user_model
from uuid import uuid4
from muco_django.utils import UploadByFieldCount

User = get_user_model()

class Brief(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    company = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=1000)
    due_date = models.DateTimeField()
    budget = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.title

class BriefImage(models.Model):
    brief = models.ForeignKey(Brief, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField()