from habitacion import views
from rest_framework import routers
from django.urls import path, include
from habitacion.views.habitacion import HabitacionViewSet

router = routers.DefaultRouter()
router.register(r"habitaciones", HabitacionViewSet, "habitaciones")

urlpatterns = [
    path(r"", include(router.urls)),
]
