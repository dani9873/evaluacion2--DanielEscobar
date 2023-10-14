from django.db import models
from cliente.models import Cliente
from habitacion.models import Habitacion

# Create your models here.

class Reservacion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    tipo_cliente = models.CharField(max_length=20)  # comun o corporativo
    forma_pago = models.CharField(max_length=20)  # contado o tarjeta de crédito
    fecha_hora_entrada = models.DateTimeField()
    fecha_hora_salida = models.DateTimeField()
    adultos = models.PositiveIntegerField()
    ninos = models.PositiveIntegerField()
    edad_ninos = models.PositiveIntegerField()
    desayunos_buffete = models.PositiveIntegerField()
    dias_renta_auto = models.PositiveIntegerField()
    codigo_tarifa_unico = models.CharField(max_length=20, null=True, blank=True)
    
    def __str__(self):
        """Return cliente."""
        return self.cliente.nombre