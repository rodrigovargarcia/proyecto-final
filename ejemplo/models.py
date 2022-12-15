from django.db import models

class Familiar(models.Model):
    
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()

    def __str__(self):
      return f"{self.nombre}, {self.numero_pasaporte}, {self.id}"

class Mascota(models.Model):

    raza = models.CharField(max_length=50)
    edad = models.IntegerField()

    def __str__(self):
      return f"{self.raza}, {self.edad}"