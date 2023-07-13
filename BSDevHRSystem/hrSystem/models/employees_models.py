from django.db import models
from django.core.validators import MinValueValidator,MaxLengthValidator,RegexValidator
from django.urls import reverse
from django.contrib.auth.models import User



def from_100000000():
    """ Returne the next default value for the employe_id"""
    largest = Employee.objects.all().order_by('employee_id').last()
    if not largest:
        return 100000000
    return largest.employee_id + 1

phone_validator= RegexValidator(regex='[234][0-9]{3}-[0-9]{4}',message="Enter a valid phone number")
cin_validator = RegexValidator(regex='[1-9][0-9]{9}',message='Enter a valid CIN number')
nif_validator = RegexValidator(regex='[0]{2}[1-9]-[0-9]{3}-[0-9]{3}-[0-9]',message='Enter a valid NIF number')

# choices
TYPE_CHOICES_PAIEMENT=(
        ('VIREMENT','VIREMENT'),
        ('CHEQUE','CHEQUE')
    )

TYPE_CHOICES_SEX = (
        ('M','Male'),
        ('F','Female')
    )

# Create your models here.
class Employee(models.Model):
    #To specify that the admin user should not be considered as an employee in the Employee model, you can add a condition to   while creating the OneToOne relationship.
    user = models.OneToOneField(User, on_delete=models.CASCADE,limit_choices_to={'is_superuser':False},related_name='employees',null=True,blank=True)
    employee_id = models.IntegerField(unique=True,null=False,validators=[MinValueValidator(100000000)],default=from_100000000)
    first_name = models.CharField(max_length=128,null=False,blank=False)
    last_name = models.CharField(max_length=128,null=False,blank=False)
    sex = models.CharField(max_length=15,null=False,blank=False,choices=TYPE_CHOICES_SEX)
    email = models.EmailField(max_length=128,unique=True)
    cin = models.IntegerField(unique=True,null=False,blank=False,validators=[cin_validator])
    nif = models.CharField(unique=True,max_length=13,null=False,blank=False,validators=[nif_validator])
    phone1 = models.CharField(unique=True,max_length=9,null=False,blank=False,validators=[phone_validator])
    phone2 = models.CharField(unique=True,max_length=9,validators=[phone_validator])
    birth_date = models.DateField(null=False,blank=False)
    hire_date = models.DateField()
    manager_id = models.ForeignKey('self',on_delete=models.CASCADE,related_name='employees',null=True,blank=True)
    service_id = models.ForeignKey('Service',on_delete=models.CASCADE,related_name='employees',null=True,blank=True)
    status_id = models.ForeignKey('Status',on_delete=models.CASCADE,related_name='employees')
    assurance_id = models.ForeignKey('Assurance',on_delete=models.CASCADE,related_name='employees')
    job_id = models.ForeignKey('Job',on_delete=models.CASCADE,related_name='employees')
    bank_id = models.ForeignKey('Bank',on_delete=models.CASCADE,related_name='employees',null=True,blank=True)
    bank_account = models.IntegerField(null=True,blank=True,unique=True)
    mode_paiement = models.CharField(max_length=11,choices=TYPE_CHOICES_PAIEMENT,default='CHEQUE')

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name

    def get_absolute_url(self):
        return reverse('hrSystem:employee-list')

    class Meta:
        ordering = ['last_name']
