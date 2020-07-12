from django.db import models
from django.contrib.auth.models import User

class Lead(models.Model):
    lead_title = models.CharField(max_length=100)
    lead_text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, default='', on_delete=models.CASCADE)

    def __str__(self):
        return self.lead_title