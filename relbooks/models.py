from django.db import models
from books.models import Book
from users.models import User

NULLABLE = {'null': True, 'blank': True}


class RelBook(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='relbooks',
        verbose_name="Книга",
        help_text="Выберите книгу"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='relbooks',
        verbose_name="Пользователь",
        help_text="Выберите пользователя"
    )
    release_date = models.DateField(
        auto_now_add=True,
        verbose_name="Дата выдачи",
        help_text="Введите дату выдачи книги"
    )
    return_date = models.DateField(
        verbose_name="Дата возврата",
        help_text="Введите дату возврата книги",
        **NULLABLE
    )

    class Meta:
        verbose_name = "Выдача книги"
        verbose_name_plural = "Выдачи книг"
        ordering = ["book"]

    def __str__(self):
        return f"{self.book.title} - {self.user.username}"
