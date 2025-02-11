from django.db import models

class Plastics(models.Model):
    code_sbk = models.CharField(max_length=20)
    name_sbk = models.CharField(max_length=50)
    code_contractor = models.CharField(max_length=20)
    name_contractor = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    note = models.TextField()

    def __str__(self):
        return self.code_sbk

class Stocks(models.Model):
    name = models.ForeignKey(Plastics, on_delete=models.CASCADE)
    quantity_3050 = models.IntegerField()
    quantity_2440 = models.IntegerField()
    quantity_4200 = models.IntegerField()
    quantity_rol = models.IntegerField()




