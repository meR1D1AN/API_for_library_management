from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RelBookViewSet

# Создаем роутер и регистрируем наш ViewSet
router = DefaultRouter()
router.register(r"", RelBookViewSet, basename="relbook")

urlpatterns = [
    # Включаем маршруты из роутера
    path("", include(router.urls)),
]
