from cliente import views
from rest_framework import routers
from django.urls import path, include
from cliente.views.cliente import ClienteViewSet

router = routers.DefaultRouter()
router.register(r"clientes", ClienteViewSet, "clientes")

urlpatterns = [
    path(r"", include(router.urls)),
]
