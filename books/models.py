from django.db import models

from authors.models import Author

NULLABLE = {'null': True, 'blank': True}


class Book(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название книги",
        help_text="Введите название книги"
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books',
        verbose_name="Автор книги",
        help_text="Выберите автора книги"
    )
    genre = models.CharField(
        max_length=255,
        verbose_name="Жанр книги",
        help_text="Введите жанр книги",
        **NULLABLE
    )
    description = models.TextField(
        verbose_name="Описание книги",
        help_text="Введите описание книги",
        **NULLABLE
    )
    published_date = models.CharField(
        max_length=10,
        verbose_name="Дата публикации книги",
        help_text="Введите год публикации книги, или же полную дату, в формате ДД.ММ.ГГГГ",
        **NULLABLE
    )
    isbn = models.CharField(
        max_length=13,
        unique=True,
        verbose_name="ISBN книги",
        help_text="Введите ISBN книги, если знаете его",
        **NULLABLE
    )

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ["title"]

    def __str__(self):
        return f"{self.title} - {self.author}"
