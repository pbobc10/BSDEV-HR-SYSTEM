from django.db import models
from django.urls import reverse
from .employees_models import Employee
from django.core.validators import MinValueValidator,MaxValueValidator
from datetime import date, timedelta


class Leave(models.Model):
    # choices
    TYPE_CHOICES_LEAVE=(
        ('SICK LEAVE','SICK LEAVE'),
        ('VACATION','VACATION'),
        ('MATERNITY','MATERNITY'),
        ('PATERNITY','PATERNITY'),
        ('OTHER','OTHER')
    )

    TYPE_CHOICES_LEAVE_STATUS = (
        ('PENDING','PENDING'),
        ('APPROVED','APPROVED'),
        ('REJECTED','REJECTED'),
    )

    employee_id = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='leaves')
    start_date = models.DateField(validators=[MinValueValidator(date.today())])
    end_date = models.DateField()
    reason = models.CharField(max_length=40,null=False,blank=False,choices=TYPE_CHOICES_LEAVE)
    comment = models.CharField(max_length=255,null=True,blank=True)
    status = models.CharField(max_length=20,choices=TYPE_CHOICES_LEAVE_STATUS,default='PENDING')
    can_edit = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('hrSystem:leave-list')