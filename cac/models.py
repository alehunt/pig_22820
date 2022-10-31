from ast import mod
from email.policy import default
from tabnanny import verbose
from django.db import models


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellido = models.CharField(max_length=150, verbose_name='Apellido')
    email = models.EmailField(max_length=150, verbose_name='Email')
    dni = models.BigIntegerField(verbose_name='DNI')
