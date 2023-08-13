from django.db import models
import datetime



class DaysOff(models.Model):
    day = models.DateField(blank=False,null=False,unique=True)
    description = models.CharField(max_length=256,blank=False,null=False,unique=True)
    fiscal_year = models.CharField(max_length=9,blank=False,null=True,unique=False)

    

  
    

        
