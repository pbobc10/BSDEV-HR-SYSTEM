from django.db import models
from django.urls import reverse


class Departement(models.Model):
    departement_name = models.CharField(max_length=128,null=False,blank=False)
    location_id = models.ForeignKey('Location',on_delete=models.CASCADE,related_name='departements')
    manager_id = models.OneToOneField('Employee',on_delete=models.CASCADE,related_name='departements',unique=True,null=True,blank=True)

    def __str__(self) -> str:
        return self.departement_name
    
    def get_absolute_url(self):
        return reverse('hrSystem:departement-list')

        
