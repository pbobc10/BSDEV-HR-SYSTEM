from django.db import models
from django.urls import reverse

class Service(models.Model):
    service_name = models.CharField(max_length=128,unique=True,null=False,blank=False)
    departement_id = models.ForeignKey('Departement',on_delete=models.CASCADE,related_name='services')

    def __str__(self) -> str:
        return self.service_name

    def get_absolute_url(self):
        return reverse('hrSystem:service-list')