from django.db import models
from django.core.validators import MinValueValidator,MaxLengthValidator,RegexValidator
from django.urls import reverse



def from_100000000():
    """ Returne the next default value for the employe_id"""
    largest = Employee.objects.all().order_by('employe_id').last()
    if not largest:
        return 100000000
    return largest.employe_id + 1

phone_validator= RegexValidator(regex='[234][0-9]{3}-[0-9]{4}',message="Enter a valid phone number")
cin_validator = RegexValidator(regex='[1-9][0-9]{9}',message='Enter a valid CIN number')
nif_validator = RegexValidator(regex='[0]{2}[1-9]-[0-9]{3}-[0-9]{3}-[0-9]',message='Enter a valid NIF number')

# Create your models here.
class Employee(models.Model):
    employe_id = models.IntegerField(unique=True,null=False,validators=[MinValueValidator(100000000)],default=from_100000000)
    last_name = models.CharField(max_length=128,null=False,blank=False)
    first_name = models.CharField(max_length=128,null=False,blank=False)
    email = models.EmailField(max_length=128)
    cin = models.IntegerField(null=False,blank=False,validators=[cin_validator])
    nif = models.CharField(max_length=13,null=False,blank=False,validators=[nif_validator])
    phone1 = models.CharField(max_length=9,null=False,blank=False,validators=[phone_validator])
    phone2 = models.CharField(max_length=9,validators=[phone_validator])
    birth_date = models.DateField(null=False,blank=False)
    hire_date = models.DateField()
    #salary = models.DecimalField(max_digits=10,decimal_places=2,null=False,blank=False,validators=[MinValueValidator(1000.00),])
    manager_id = models.ForeignKey('self',on_delete=models.CASCADE,related_name='employees',null=True,blank=True)
    service_id = models.ForeignKey('Service',on_delete=models.CASCADE,related_name='employees',null=True,blank=True)
    status_id = models.ForeignKey('Status',on_delete=models.CASCADE,related_name='employees')
    assurance_id = models.ForeignKey('Assurance',on_delete=models.CASCADE,related_name='employees')
    job_id = models.ForeignKey('Job',on_delete=models.CASCADE,related_name='employees')
    bank_id = models.ForeignKey('Bank',on_delete=models.CASCADE,related_name='employees',null=True,blank=True)
    bank_account = models.IntegerField(null=True,blank=True)

    TYPE_CHOICES=(
        ('VIREMENT','VIREMENT'),
        ('CHEQUE','CHEQUE')
    )

    mode_paiement = models.CharField(max_length=11,choices=TYPE_CHOICES)

    def __str__(self) -> str:
        return self.last_name

    def get_absolute_url(self):
        return reverse('hrSystem:employee-list')

    class Meta:
        ordering = ['last_name']
