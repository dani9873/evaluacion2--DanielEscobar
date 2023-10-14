from rest_framework import serializers
from ..models import Reservacion

class ReservacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservacion
        fields = '__all__'
        
    def validate(self, data):
        # Lógica de validación para la forma de pago
        forma_pago = data.get('forma_pago')

        if forma_pago not in ['Al contado', 'Tarjeta de crédito']:
            raise serializers.ValidationError("La forma de pago debe ser 'Al contado' o 'Tarjeta de crédito'.")

        # Validación de fechas de entrada y salida
        fecha_entrada = data.get('fecha_hora_entrada')
        fecha_salida = data.get('fecha_hora_salida')

        if fecha_salida <= fecha_entrada:
            raise serializers.ValidationError("La fecha de salida debe ser posterior a la fecha de entrada.")
        
        # Lógica de validación para la cantidad de adultos y niños
        num_adultos = data.get('num_adultos')
        num_ninos = data.get('num_ninos')
        edad_ninos = data.get('edad_ninos')

        if num_adultos < 1:
            raise serializers.ValidationError("Debe haber al menos un adulto en la reservación.")

        if num_ninos < 0:
            raise serializers.ValidationError("La cantidad de niños no puede ser negativa.")

        if num_ninos > 0 and not edad_ninos:
            raise serializers.ValidationError("Debes proporcionar la edad de los niños.")

        if num_ninos > 0 and min(edad_ninos) >= 5:
            raise serializers.ValidationError("Los niños con 5 años o más deben considerarse adultos.")
        
        # Validación de días de renta de auto
        dias_renta_auto = data.get('dias_renta_auto')

        if dias_renta_auto < 0:
            raise serializers.ValidationError("El número de días de renta de auto no puede ser negativo.")
        
        # Validación de código de tarifa único
        codigo_tarifa = data.get('codigo_tarifa')

        if not codigo_tarifa and data.get('cliente').tipo_cliente == 'corporativo':
            raise serializers.ValidationError("Los clientes corporativos deben proporcionar un código de tarifa único.")
        

        return data