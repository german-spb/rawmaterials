from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, User

class Plastics(models.Model):
    code_sbk = models.CharField(max_length=20, unique=True)
    name_sbk = models.CharField(max_length=50, blank=True, default='')
    code_contractor = models.CharField(max_length=20, blank=True, default='')
    name_contractor = models.CharField(max_length=50, blank=True, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    note = models.TextField(blank=True, default='')

    def __str__(self):
        return self.code_sbk

class Stocks(models.Model):
    plastic = models.ForeignKey(Plastics, on_delete=models.CASCADE, related_name='plastics')
    quantity_3050 = models.IntegerField()
    quantity_2440 = models.IntegerField()
    quantity_4200 = models.IntegerField()
    quantity_rol = models.IntegerField()


class Result(models.Model):
    plastic = models.CharField(max_length=50)
    quantity_sheet = models.IntegerField()
    quantity_rol = models.IntegerField()
    total = models.IntegerField()



