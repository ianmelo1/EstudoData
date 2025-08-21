from datetime import timezone

from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone



class Carro(models.Model):
   modelo = models.CharField(max_length=50, null=False)
   marca = models.CharField(max_length=50, null=False)
   ano = models.PositiveIntegerField(validators=[MinValueValidator(2000)], null=False)
   valor = models.FloatField(null=False)
   data_cadastro = models.DateTimeField(default=timezone.now,null=False)