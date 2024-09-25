from django.db import models

NULLABLE = {"null": True, "blank": True}


class Author(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Имя и фамилия автора книги",
        help_text="Введите имя и фамилию автора книги",
    )
    bio = models.TextField(
        verbose_name="Биография", help_text="Введите текст биографии", **NULLABLE
    )
    date_of_birth = models.DateField(
        verbose_name="Дата рождения",
        help_text="Введите дату рождения автора, в формате ГОД-МЕСЯЦ-ДЕНЬ, если она известна",
        **NULLABLE,
    )

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        ordering = ["name"]

    def __str__(self):
        return f"Автор - {self.name}"
