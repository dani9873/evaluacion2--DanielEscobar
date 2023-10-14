from django.db import models


# Create your models here.

class Habitacion(models.Model):
    TIPOS_HABITACION = (
        ('simple', 'Simple'),
        ('doble', 'Doble'),
        ('triple', 'Triple'),
        ('matrimonial', 'Matrimonial'),
    )
    tipo = models.CharField(max_length=20, choices=TIPOS_HABITACION)
    tarifa = models.DecimalField(max_digits=10, decimal_places=2)
    fotos = models.ImageField(upload_to='habitacion_fotos/', null=True, blank=True)
    
    def __str__(self):
        """Return tipo."""
        return self.tipo