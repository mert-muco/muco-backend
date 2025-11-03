from django.db import models
from uuid import uuid4
from brief_app.models import Brief
from bid_app.models import Bid
from django.contrib.auth import get_user_model

User = get_user_model()

class Order(models.Model):
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    brief = models.OneToOneField(Brief, on_delete=models.CASCADE)
    bid = models.OneToOneField(Bid, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    video = models.FileField(null=True, blank=True)