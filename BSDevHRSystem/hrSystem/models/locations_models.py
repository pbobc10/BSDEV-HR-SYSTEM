from django.db import models
from django.core.validators import RegexValidator
from django.urls import reverse

postal_code_validator = RegexValidator(regex='[1-9][0-9]{3}',message='Enter a valid postal code')

class Location(models.Model):
    street_address = models.CharField(max_length=256)
    postal_code = models.CharField(max_length=4,validators=[postal_code_validator])
    city = models.CharField(max_length=128)
    state_province = models.CharField(max_length=128)
    country_id = models.ForeignKey('Country',on_delete=models.CASCADE,related_name='locations')

    def get_absolute_url(self):
        return reverse('hrSystem:location-list')
    
    def __str__(self) -> str:
        return self.street_address
        
