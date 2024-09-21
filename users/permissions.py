from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Разрешает доступ только администратору или владельцу учетной записи.
    """

    def has_object_permission(self, request, view, obj):
        # Разрешаем доступ админу или владельцу объекта (пользователю)
        return request.user.is_staff or obj == request.user
