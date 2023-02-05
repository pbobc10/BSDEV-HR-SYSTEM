from django.db import models
from django.urls import reverse

class Status(models.Model):
    status_type = models.CharField(max_length=30,unique=True,null=False,blank=False)

    def __str__(self) -> str:
        return self.status_type

    def get_absolute_url(self):
        return reverse('hrSystem:status-list')