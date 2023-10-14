from rest_framework import serializers, views, routers
from ..models import Cliente
from django.contrib.auth.models import User
import re

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        

def validate(self, data):
        # Lógica de validación para el tipo de cliente
        tipo_cliente = data.get('tipo_cliente')

        if tipo_cliente not in ['común', 'corporativo']:
            raise serializers.ValidationError("El tipo de cliente debe ser 'común' o 'corporativo'.")

         # Validación de formato de DPI o pasaporte
        dpi_pasaporte = data.get('dpi_o_pasaporte')
        if not validar_formato_dpi_pasaporte(dpi_pasaporte):
            raise serializers.ValidationError("El formato de DPI o pasaporte es inválido.")

        # Validación de formato de NIT
        nit = data.get('nit')
        if not validar_formato_nit(nit):
            raise serializers.ValidationError("El formato de NIT es inválido.")

        # Validación de formato de correo electrónico
        correo_electronico = data.get('correo_electronico')
        if not validar_formato_correo(correo_electronico):
            raise serializers.ValidationError("El formato de correo electrónico es inválido.")

        # Validación de formato de teléfono
        telefono = data.get('telefono')
        if not validar_formato_telefono(telefono):
            raise serializers.ValidationError("El formato de teléfono es inválido.")

        return data
    
def validar_formato_dpi_pasaporte(dpi_pasaporte):
    formato_valido = re.match(r'^[0-9A-Za-z]+$', dpi_pasaporte)
    return formato_valido is not None

def validar_formato_nit(nit):
    formato_valido = re.match(r'^[0-9A-Za-z\-]+$', nit)
    return formato_valido is not None

def validar_formato_correo(correo_electronico):
    formato_valido = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', correo_electronico)
    return formato_valido is not None


def validar_formato_telefono(telefono):
    formato_valido = re.match(r'^[0-9]+$', telefono)
    return formato_valido is not None
