from django.apps import AppConfig


class RelBooksConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "relbooks"
    verbose_name = "Выдача книги"
    verbose_name_plural = "Выдачи книг"
