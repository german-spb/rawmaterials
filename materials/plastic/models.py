from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, User
from django.utils.timezone import now

class Plastics(models.Model):
    code_sbk = models.CharField(max_length=20, unique=True)
    name_sbk = models.CharField(max_length=50, blank=True, default='')
    code_contractor = models.CharField(max_length=20, blank=True, default='')
    name_contractor = models.CharField(max_length=50, blank=True, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    note = models.TextField(blank=True, default='')
    class Meta:
        ordering = ['code_sbk']

    def __str__(self):
        return self.code_sbk


class Stocks(models.Model):
    plastic = models.ForeignKey(Plastics, on_delete=models.CASCADE, related_name='plastics')
    quantity_3050 = models.IntegerField()
    quantity_2440 = models.IntegerField()
    quantity_4200 = models.IntegerField()
    quantity_rol = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True,  editable=False)
    class Meta:
        ordering = ['plastic']


class Result(models.Model):
    plastic = models.CharField(max_length=50)
    quantity_sheet = models.IntegerField()
    quantity_rol = models.IntegerField()
    total = models.IntegerField()

class Chipboard(models.Model):
    thickness = models.CharField(max_length=50)
    format = models.CharField(max_length=100)
    aqua = models.CharField(max_length=10)
    sort = models.CharField(max_length=10)
    unit = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    class Meta:
        ordering = ['thickness', 'aqua',]

    def __str__(self):
        return self.thickness


class Glue(models.Model):
    name = models.CharField(max_length=200)
    main = models.BooleanField()
    type = models.CharField(max_length=50)
    supplier = models.CharField(max_length=150)
    pack = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    line = models.CharField(max_length=250)

    class Meta:
        ordering = ['supplier',]

    def __str__(self):
        return self.line

class Pack(models.Model):
    name = models.CharField(max_length=200)
    unit = models.CharField(max_length=50)
    supplier = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    note = models.TextField(blank=True, default='')

    class Meta:
        ordering = ['name',]

class Phone(models.Model):
    surname = models.CharField(max_length=100, blank=True, default='')
    first_name = models.CharField(max_length=100, blank=True, default='')
    second_name = models.CharField(max_length=100, blank=True, default='')
    department = models.CharField(max_length=200, blank=True, default='')
    phone = models.CharField(max_length=50,blank=True, default='')
    phone_service = models.CharField(max_length=50, blank=True, default='')

    class Meta:
        ordering = ['surname',]
