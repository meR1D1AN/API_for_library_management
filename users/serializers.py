import re
from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, style={"input_type": "password"}
    )
    phone = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "password",
            "date_of_birth",
            "phone",
            "bio",
        ]

    def validate_password(self, value):
        """
        Валидация пароля на соответствие требованиям
        """
        if len(value) < 8:
            raise serializers.ValidationError("Пароль должен быть не менее 8 символов.")

        if len(re.findall(r"[A-Z]", value)) < 2:
            raise serializers.ValidationError(
                "Пароль должен содержать минимум 2 заглавные буквы."
            )

        if len(re.findall(r"\d", value)) < 2:
            raise serializers.ValidationError(
                "Пароль должен содержать минимум 2 цифры."
            )

        if len(re.findall(r'[!@#$%^&*(),.?":{}|<>]', value)) < 1:
            raise serializers.ValidationError(
                "Пароль должен содержать минимум 1 специальный символ."
            )

        return value

    def validate(self, data):
        """
        Проверяем, что при обновлении или частичном обновлении передан пароль
        """
        if self.instance and ("password" not in data or not data.get("password")):
            raise serializers.ValidationError(
                "Пароль обязателен при обновлении учетной записи."
            )
        return data

    def validate_phone(self, value):
        """
        Валидация и очистка номера телефона от пробелов.
        Допускается формат +79991234567 или с пробелами, которые будут удалены.
        """
        # Убираем все пробелы
        phone = re.sub(r"\s+", "", value)

        # Проверяем, что номер соответствует формату +7XXXXXXXXXX
        if not re.match(r"^\+7\d{10}$", phone):
            raise serializers.ValidationError(
                "Номер телефона должен быть в формате +7XXXXXXXXXX без пробелов."
            )

        return phone

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)  # Хешируем пароль
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        phone = validated_data.get("phone", None)

        # Если есть новый пароль, обновляем его
        if password:
            self.validate_password(password)
            instance.set_password(password)

        # Обновляем номер телефона, если он передан
        if phone:
            validated_data["phone"] = self.validate_phone(phone)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name"]
