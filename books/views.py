from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, AllowAny

from users.permissions import IsOwnerOrAdmin
from .models import Book
from .paginators import StandardResultsSetPagination
from .serializers import BookSerializer

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = StandardResultsSetPagination
    # Включаем фильтрацию и поиск
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # Указываем, по каким полям можно делать фильтрацию
    filterset_fields = ['author', 'genre', 'published_date']
    # Указываем, по каким полям можно делать поиск (поиск по названию)
    search_fields = ['title']

    @swagger_auto_schema(
        operation_description="Получить список всех книг",
        responses={200: BookSerializer(many=True)},
        tags=["3. Книги"],
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
        operation_description="""
        Создание новой книги
        Необходимо передать имя книги, автора, жанра и дату публикации
        """,
        request_body=BookSerializer,
        responses={201: BookSerializer},
        tags=["3. Книги"],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Получить информацию о книге",
        responses={200: BookSerializer},
        tags=["3. Книги"],
        manual_parameters=[
            openapi.Parameter(
                name='id',
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                description="Укажите ID книги",
            ),
        ],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Обновить информацию о книге",

        responses={200: BookSerializer},
        tags=["3. Книги"],
        manual_parameters=[
            openapi.Parameter(
                name='id',
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                description="Укажите ID книги",
            ),
        ],
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Частичное обновление информации о книге",
        responses={200: BookSerializer},
        tags=["3. Книги"],
        manual_parameters=[
            openapi.Parameter(
                name='id',
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                description="Укажите ID книги",
            ),
        ],
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Удалить книгу",
        responses={204: None},
        tags=["3. Книги"],
        manual_parameters=[
            openapi.Parameter(
                name='id',
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                description="Укажите ID книги",
            ),
        ],
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAuthenticated(), IsOwnerOrAdmin()]
