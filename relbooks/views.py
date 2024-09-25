from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response

from books.models import Book
from books.paginators import StandardResultsSetPagination
from users.permissions import IsOwnerOrAdmin
from .models import RelBook
from .serializers import RelBookSerializer, RelBookCreateSerializer


class RelBookViewSet(viewsets.ModelViewSet):
    queryset = RelBook.objects.all()
    serializer_class = RelBookSerializer
    pagination_class = StandardResultsSetPagination

    @swagger_auto_schema(
        operation_description="Получить список всех выдач книг",
        responses={200: RelBookSerializer(many=True)},
        tags=["4. Выдача книги"],
        manual_parameters=[
            openapi.Parameter(
                name="page",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Номер страницы",
                default=1,
            ),
            openapi.Parameter(
                name="page_size",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Количество элементов на странице",
                default=10,
            ),
        ],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="""
        Создание выдачи книги
        Необходимо предоставить ID книги и ID пользователя. Дата выдачи ставится автоматически.
        """,
        request_body=RelBookCreateSerializer,
        responses={201: RelBookCreateSerializer},
        tags=["4. Выдача книги"],
    )
    def create(self, request, *args, **kwargs):
        # return super().create(request, *args, **kwargs)
        data = request.data
        book = Book.objects.get(id=data["book_id"])

        # Проверка, что книга доступна для выдачи
        if book.count == 0:
            raise ValidationError(f"Книга {book.title} отсутствует в наличии.")

        response = super().create(request, *args, **kwargs)

        # Уменьшение количества книг после успешного создания выдачи
        book.count -= 1
        book.save()

        # Проверка, осталось ли 5 книг
        if book.count == 5:
            return Response(
                {
                    "message": f"Книга '{book.title}' выдана. Осталось 5 экземпляров.",
                    "data": response.data,
                },
                status=status.HTTP_201_CREATED,
            )

        return response

    @swagger_auto_schema(
        operation_description="Получить информаци о выдачи книги",
        responses={200: RelBookSerializer},
        tags=["4. Выдача книги"],
        manual_parameters=[
            openapi.Parameter(
                name="id",
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                description="Укажите ID выдачи книги",
            ),
        ],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Обновить информацию о выдачи книги",
        responses={200: RelBookSerializer},
        tags=["4. Выдача книги"],
        manual_parameters=[
            openapi.Parameter(
                name="id",
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                description="Укажите ID выдачи книги",
            ),
        ],
    )
    def update(self, request, *args, **kwargs):
        # Метод для обновления информации о выдаче книги
        instance = self.get_object()

        # Проверка, была ли возвращена книга
        if "return_date" in request.data and request.data["return_date"]:
            if not instance.return_date:  # Если книга была возвращена впервые
                instance.book.count += 1
                instance.book.save()

        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Частичное обновление информации о выдачи книги",
        responses={200: RelBookSerializer},
        tags=["4. Выдача книги"],
        manual_parameters=[
            openapi.Parameter(
                name="id",
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                description="Укажите ID выдачи книги",
            ),
        ],
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Удалить выдачу книги",
        responses={204: None},
        tags=["4. Выдача книги"],
        manual_parameters=[
            openapi.Parameter(
                name="id",
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                description="Укажите ID выдачи книги",
            ),
        ],
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def get_permissions(self):
        if self.action == ["list", "destroy"]:
            return [IsAdminUser()]
        return [IsAuthenticated(), IsOwnerOrAdmin()]
