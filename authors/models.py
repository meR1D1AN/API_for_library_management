from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Author(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Ф. И. О. автора книги",
        help_text="Введите полное Ф. И. О. автора книги"
    )
    bio = models.TextField(
        verbose_name="Биография",
        help_text="Введите текст биографии",
        **NULLABLE
    )
    date_of_birth = models.DateField(
        verbose_name="Дата рождения",
        help_text="Введите дату рождения, в формате ГОД-МЕСЯЦ-ДЕНЬ",
        **NULLABLE
    )

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
        ordering = ["name"]

    def __str__(self):
        return f"Автор - {self.name}"
