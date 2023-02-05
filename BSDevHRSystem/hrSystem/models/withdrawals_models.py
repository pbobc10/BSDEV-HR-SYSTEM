from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse

class Withdrawal(models.Model):
    withdrawal_name = models.CharField(max_length=10)
    withdrawal_amount = models.DecimalField(max_digits=15,decimal_places=2,default=0.00,null=False,blank=False,validators=[MinValueValidator(0.00)])
    description = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.withdrawal_name

    def get_absolute_url(self):
        return reverse('hrSystem:withdrawal-list')