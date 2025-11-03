from django.db import models
from brief_app.models import Brief
from django.contrib.auth import get_user_model
from muco_django.utils import UploadByFieldCount
from uuid import uuid4

User = get_user_model()

class Bid(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    brief = models.ForeignKey(Brief, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.FileField(upload_to=UploadByFieldCount('brief'))
    vision = models.CharField(max_length=700)
    asked_budget = models.DecimalField(max_digits=12, decimal_places=2)
    ai_score = models.PositiveSmallIntegerField(blank=True, null=True)