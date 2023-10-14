# Django REST Framework
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet


# serializers
from habitacion.serializers.habitacion import HabitacionSerializer

# Models
from habitacion.models import Habitacion

class HabitacionViewSet(viewsets.ModelViewSet):
    serializer_class = HabitacionSerializer
    
    def get_queryset(self):
        """Restrict list to public-only."""
        queryset = Habitacion.objects.all()
        return queryset
