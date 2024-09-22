from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from books.paginators import StandardResultsSetPagination
from .models import User
from .serializers import UserSerializer
from .permissions import IsOwnerOrAdmin


class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        tags=["1. Авторизация и пользователь"],
        operation_description="""
        Авторизация для получения токена
        Необходимо предоставить логин и пароль пользователя
        """,

    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CustomTokenRefreshView(TokenRefreshView):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        tags=["1. Авторизация и пользователь"],
        operation_description="Авторизация для обновления токена, необходимо предоставить прошлый токен",

    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = StandardResultsSetPagination

    @swagger_auto_schema(
        operation_description="Получить список всех пользователей",
        responses={200: UserSerializer(many=True)},
        tags=["1. Авторизация и пользователь"],
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
        Регистрация нового пользователя
        Необходимые поля для заполнения: first_name, last_name, email, password, phone
        """,
        request_body=UserSerializer,
        responses={201: UserSerializer},
        tags=["1. Авторизация и пользователь"],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Получить информацию о пользователе",
        responses={200: UserSerializer},
        tags=["5. Пользователь"],
        manual_parameters=[
            openapi.Parameter(
                name='id',
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                description="Укажите ID пользователя",
            ),
        ],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Обновить информацию о пользователе",
        responses={200: UserSerializer},
        tags=["5. Пользователь"],
        manual_parameters=[
            openapi.Parameter(
                name='id',
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                description="Укажите ID пользователя",
            ),
        ],
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Частичное обновление информации о пользователе",
        responses={200: UserSerializer},
        tags=["5. Пользователь"],
        manual_parameters=[
            openapi.Parameter(
                name='id',
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                description="Укажите ID пользователя",
            ),
        ],
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Удалить пользователя",
        responses={204: None},
        tags=["5. Пользователь"],
        manual_parameters=[
            openapi.Parameter(
                name='id',
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                description="Укажите ID пользователя",
            ),
        ],
    )
    def destroy(self, request, *args, **kwargs):
        # Дополнительно проверим пароль при удалении, если нужно
        if 'password' not in request.data:
            return Response({"error": "Пароль обязателен для удаления пользователя."},
                            status=status.HTTP_400_BAD_REQUEST)

        # Валидация пароля
        user = self.get_object()
        if not user.check_password(request.data['password']):
            return Response({"error": "Неправильный пароль."}, status=status.HTTP_400_BAD_REQUEST)

        return super().destroy(request, *args, **kwargs)

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated(), IsOwnerOrAdmin()]
