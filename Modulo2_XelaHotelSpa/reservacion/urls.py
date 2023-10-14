from reservacion import views
from rest_framework import routers
from django.urls import path, include
from reservacion.views.reservacion import ReservacionViewSet

router = routers.DefaultRouter()
router.register(r"reservaciones", ReservacionViewSet, "reservaciones")

urlpatterns = [
    path(r"", include(router.urls)),
]