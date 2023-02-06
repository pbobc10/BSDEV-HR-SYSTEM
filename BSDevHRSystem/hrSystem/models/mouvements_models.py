from django.db import models
from django.urls import reverse

class Mouvement(models.Model):
    mouvement_type = models.CharField(max_length=10,null=False,blank=False)
    description = models.CharField(max_length=256,null=False,blank=False)

    def __str__(self) -> str:
        return self.mouvement_type
    
    def get_absolute_url(self):
        return reverse('hrSystem:mouvement-list')