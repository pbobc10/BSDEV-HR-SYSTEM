from django.db import models
from django.urls import reverse

class Region(models.Model):
    region_name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.region_name

    def get_absolute_url(self):
        return reverse('hrSystem:region-list')