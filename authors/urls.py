from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet

# Создаем роутер и регистрируем наш ViewSet
router = DefaultRouter()
router.register(r'', AuthorViewSet, basename='authors')

urlpatterns = [
    # Включаем маршруты из роутера
    path('', include(router.urls)),
]
