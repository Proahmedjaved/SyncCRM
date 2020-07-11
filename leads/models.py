from django.db import models

class Lead(models.Model):
    lead_title = models.CharField(max_length=100)
    lead_text = models.CharField(max_length=200)
    created_at = models.DateTimeField('date created')

    def __str__(self):
        return self.lead_title