from django.db import models

class Plastics(models.Model):
    code_sbk = models.CharField(max_length=20)
    name_sbk = models.CharField(max_length=50)
    code_contractor = models.CharField(max_length=20)
    name_contractor = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity = models.IntegerField()
