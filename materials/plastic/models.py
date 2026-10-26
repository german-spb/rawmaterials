from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, User
from django.utils.timezone import now
from numpy.lib.recfunctions import require_fields


class Plastics(models.Model):
    code_sbk = models.CharField(max_length=20, unique=True)
    name_sbk = models.CharField(max_length=50, blank=True, default='')
    code_contractor = models.CharField(max_length=20, blank=True, default='')
    name_contractor = models.CharField(max_length=50, blank=True, default='')
    surface = models.CharField(max_length=50, blank=True, default='')
    price_03 = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    price_05 = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    fabricator = models.CharField(max_length=50, blank=True, default='')
    note = models.TextField(blank=True, default='')
    class Meta:
        ordering = ['code_sbk']

    def __str__(self):
        return self.code_sbk


class Stocks(models.Model):
    plastic = models.ForeignKey(Plastics, on_delete=models.CASCADE, related_name='plastics')
    quantity_3050 = models.FloatField()
    quantity_2440 = models.FloatField()
    quantity_4200 = models.FloatField()
    quantity_rol = models.FloatField()
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
        ordering = ['aqua', 'thickness', 'sort', ]

    def __str__(self):
        return self.thickness


class Glue(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=50)
    supplier = models.CharField(max_length=150)
    pack = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    line = models.CharField(max_length=250)

    class Meta:
        ordering = ['supplier',]

    def __str__(self):
        return self.name

class Documents(models.Model):
    glue = models.ForeignKey(Glue, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    document = models.FileField(upload_to='documents/')

class NoteGlue(models.Model):
    glue = models.ForeignKey(Glue, on_delete=models.CASCADE)
    note = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)


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

class CostPrice(models.Model):
    price_26х600х3050 = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    price_26х600х2440 = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    price_26х600х2500 = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    price_38х600х2440 = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    price_38х600х3050 = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    price_38х800х3050 = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    price_38х900х3050 = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    price_38х600х4200 = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    price_4х600х3050 = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    price_6х600х3050 = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    price_6х600х2400 = models.DecimalField(max_digits=8, decimal_places=2, default=0)

class DefectPlastic(models.Model):
    plastic = models.ForeignKey(Plastics, on_delete=models.CASCADE, related_name='code_fabricator')
    code_contractor = models.CharField(max_length=20, blank=True, default='')
    current_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    defect_plastic = models.FloatField(default=0)
    quantity_26х600х3050 = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    board_26х600х3050 = models.IntegerField(default=0)
    quantity_26х600х2440 = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    board_26х600х2440 = models.IntegerField(default=0)
    quantity_26х600х2500 = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    board_26х600х2500 = models.IntegerField(default=0)
    quantity_38х600х2440 = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    board_38х600х2440 = models.IntegerField(default=0)
    quantity_38х600х3050 = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    board_38х600х3050 = models.IntegerField(default=0)
    quantity_38х800х3050 = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    board_38х800х3050 = models.IntegerField(default=0)
    quantity_38х900х3050 = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    board_38х900х3050 = models.IntegerField(default=0)
    quantity_38х600х4200 = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    board_38х600х4200 = models.IntegerField(default=0)
    quantity_4х600х3050 = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    board_4х600х3050 = models.IntegerField(default=0)
    quantity_6х600х3050 = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    board_6х600х3050 = models.IntegerField(default=0)
    quantity_6х600х2400 = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    board_6х600х2400 = models.IntegerField(default=0)
    coast_defect_plastic = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    sum_quntity = models.FloatField(default=0)
    sum_coast_board = models.FloatField(default=0)
    total_defect_plastic = models.FloatField(default=0)
    total_coast_defect_plastic = models.FloatField(default=0)


