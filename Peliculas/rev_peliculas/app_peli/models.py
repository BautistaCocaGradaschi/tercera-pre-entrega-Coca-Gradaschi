from django.db import models

# Create your models here.
class Peliculas(models.Model):
    nombre = models.CharField(max_length=64)
    puntaje = models.IntegerField()
class Series(models.Model):
    nombre = models.CharField(max_length=64)
    puntaje = models.IntegerField()
class Actores(models.Model):
    nombre = models.CharField(max_length=64)
    puntaje = models.IntegerField()

