from django.db import models
from django.urls import reverse

class Assurance(models.Model):
    assurance_type = models.CharField(max_length=10,unique=True,null=False,blank=False)
    description = models.CharField(max_length=128,unique=True,null=True,blank=True)

    def __str__(self) -> str:
        return self.assurance_type

    def get_absolute_url(self):
        return reverse('hrSystem:assurance-list')

