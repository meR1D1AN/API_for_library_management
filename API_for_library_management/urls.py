from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

schema_view = get_schema_view(
    openapi.Info(
        title="API для управления библиотекой",
        default_version='v1.03',
        description="""
        API для управления библиотекой предоставляет возможности для управления книгами, авторами и пользователями, а также для отслеживания выдачи книг пользователям. 
        Основные функции API:
        - Поиск книг по различным критериям (название, автор, жанр и т.д.).
        - Получение списка всех книг.
        - Создание, редактирование и удаление книг.
        - Получение списка всех авторов.
        - Создание, редактирование и удаление авторов.
        - Получение информации о пользователях.
        - Регистрация и авторизация пользователей.
        - Отслеживание статуса возврата книги.
        - Запись информации о выдаче книги пользователю.
        
        Аутентификация и авторизация пользователей осуществляется с использованием JWT токенов.
        """,
        contact=openapi.Contact(email="nikita@mer1d1an.ru"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books/', include('books.urls')),
    path('api/authors/', include('authors.urls')),
    path('api/users/', include('users.urls')),
    path('api/relbooks/', include('relbooks.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
]
