from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoanViewSet

# Создаем роутер и регистрируем наш ViewSet
router = DefaultRouter()
router.register(r'', LoanViewSet, basename='loan')

urlpatterns = [
    # Включаем маршруты из роутера
    path('', include(router.urls)),
]
