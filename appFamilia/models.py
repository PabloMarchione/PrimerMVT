from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=11)
    apellido = models.CharField(max_length=11)
    fecha_nacimiento = models.DateField()
    dni = models.IntegerField()
    
    def __str__(self):
        return self.nombre
    
    
