# Django REST Framework
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet


# serializers
from reservacion.serializers.reservacion import ReservacionSerializer

# Models
from reservacion.models import Reservacion

class ReservacionViewSet(viewsets.ModelViewSet):
    serializer_class = ReservacionSerializer
    
    def get_queryset(self):
        """Restrict list to public-only."""
        queryset = Reservacion.objects.all()
        return queryset
