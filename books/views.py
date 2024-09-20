from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Book
from .paginators import StandardResultsSetPagination
from .serializers import BookSerializer

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = StandardResultsSetPagination

    @swagger_auto_schema(
        operation_description="Получить список всех книг",
        responses={200: BookSerializer(many=True)},
        tags=["Книги"],
        manual_parameters=[
            openapi.Parameter(
                name='page',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Номер страницы",
                default=1
            ),
            openapi.Parameter(
                name='page_size',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Количество элементов на странице",
                default=10
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


    @swagger_auto_schema(
        operation_description="Создание новой книги",
        request_body=BookSerializer,
        responses={201: BookSerializer},
        tags=["Книги"],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Получить информацию о книге",
        responses={200: BookSerializer},
        tags=["Книги"],
        manual_parameters=[
            openapi.Parameter(
                name='id',
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                description="Уникальный идентификатор книги",
                default="Введите ID книги",
            ),
        ],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Обновить информацию о книге",

        responses={200: BookSerializer},
        tags=["Книги"],
        manual_parameters=[
            openapi.Parameter(
                name='id',
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                description="Уникальный идентификатор книги",
                default="Введите ID книги",
            ),
        ],
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Частичное обновление информации о книге",
        responses={200: BookSerializer},
        tags=["Книги"],
        manual_parameters=[
            openapi.Parameter(
                name='id',
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                description="Уникальный идентификатор книги",
                default="Введите ID книги",
            ),
        ],
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Удалить книгу",
        responses={204: None},
        tags=["Книги"],
        manual_parameters=[
            openapi.Parameter(
                name='id',
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                description="Уникальный идентификатор книги",
                default="Введите ID книги",
            ),
        ],
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def get_permissions(self):
        if self.action == 'create' or self.action == 'list':
            return [AllowAny()]
        return [IsAuthenticated()]
