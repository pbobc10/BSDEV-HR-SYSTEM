from django.db import models
from django.urls import reverse

class Bank(models.Model):
    bank_code = models.CharField(max_length=10,unique=True,null=False,blank=False)
    routing_number_bank = models.IntegerField(unique=True,null=False,blank=False)
    description = models.CharField(max_length=256,unique=True,null=False,blank=False)

    def __str__(self) -> str:
        return self.description

    def get_absolute_url(self):
        return reverse('hrSystem:bank-list')