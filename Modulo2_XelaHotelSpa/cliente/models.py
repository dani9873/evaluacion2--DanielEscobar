from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dpi_pasaporte = models.CharField(max_length=20)
    nit = models.CharField(max_length=20)
    correo_electronico = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.TextField()
    nacionalidad = models.CharField(max_length=50)
    
    def __str__(self):
        """Return nombre."""
        return self.nombre