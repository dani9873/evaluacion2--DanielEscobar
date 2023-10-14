from rest_framework import serializers
from ..models import Habitacion

class HabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        fields = '__all__'
        
    def validate(self, data):
        # Lógica de validación para la tarifa
        tipo_habitacion = data.get('tipo_habitacion')

        if tipo_habitacion not in ['Simple', 'Doble', 'Triple', 'Matrimonial']:
            raise serializers.ValidationError("El tipo de habitación debe ser 'Simple', 'Doble', 'Triple' o 'Matrimonial'.")

        # Validación de la tarifa
        tarifa = data.get('tarifa')
        if tarifa <= 0:
            raise serializers.ValidationError("La tarifa debe ser mayor que cero.")
        
        # Regla adicional: Validar que el campo 'foto' no esté en blanco
        foto = data.get('foto')
        if not foto:
            raise serializers.ValidationError("La foto de la habitación es obligatoria.")

        return data