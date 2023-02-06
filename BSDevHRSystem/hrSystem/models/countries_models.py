from django.db import models
from django.urls import reverse

class Country(models.Model):
    country_name = models.CharField(max_length=128)
    region_id = models.ForeignKey('Region',on_delete=models.CASCADE,related_name='countries')

    def __str__(self) -> str:
        return self.country_name

    def get_absolute_url(self):
        return reverse('hrSystem:country-list')

