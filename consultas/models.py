from django.db import models

class Sintomas(models.Model):
    edad = models.IntegerField()
    caracteristicas = models.TextField()
    factores = models.TextField()

class Diagnostico(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    edad = models.IntegerField()
    sintomas = models.ForeignKey(Sintomas, on_delete=models.CASCADE, related_name='diagnosticos')

class Intervencion(models.Model):
    descripcion = models.TextField()
    estrategia = models.TextField()
    diagnostico = models.ForeignKey(Diagnostico, on_delete=models.CASCADE, related_name='intervenciones')

class Apoyo(models.Model):
    descripcion = models.TextField()
    tipos = models.CharField(max_length=100)
    diagnostico = models.ForeignKey(Diagnostico, on_delete=models.CASCADE, related_name='apoyos')