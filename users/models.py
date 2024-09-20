from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None

    first_name = models.CharField(
        max_length=60,
        verbose_name="Имя",
        help_text="Укажите имя",
    )
    last_name = models.CharField(
        max_length=60,
        verbose_name="Фамилия",
        help_text="Укажите фамилию",
        default="",
        **NULLABLE
    )
    email = models.EmailField(
        unique=True,
        verbose_name="Электронная почта",
        help_text="Укажите электронную почту",
    )
    phone = models.CharField(
        max_length=15,
        verbose_name="Телефон",
        help_text="Укажите телефон, начиная с +79991234567",
        default="",
    )
    date_of_birth = models.DateField(
        verbose_name="Дата рождения",
        help_text="Укажите дату рождения",
        **NULLABLE
    )
    bio = models.TextField(
        verbose_name="О себе",
        help_text="Расскажите о себе",
        **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
