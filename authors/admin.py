from django.contrib import admin

from authors.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "bio", "date_of_birth")
