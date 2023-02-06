from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse

class Job(models.Model):
    job_title = models.CharField(max_length=128)
    salary = models.DecimalField(max_digits=10,decimal_places=2,null=False,blank=False,validators=[MinValueValidator(1000.00)])
    
    def get_absolute_url(self):
        return reverse('hrSystem:job-list')

    def __str__(self) -> str:
        return self.job_title
