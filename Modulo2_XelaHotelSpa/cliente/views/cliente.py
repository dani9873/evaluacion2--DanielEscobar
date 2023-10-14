# Django REST Framework
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet


# serializers
from cliente.serializers.cliente import ClienteSerializer

# Models
from cliente.models import Cliente

class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    
    def get_queryset(self):
        """Restrict list to public-only."""
        queryset = Cliente.objects.all()
        return queryset
