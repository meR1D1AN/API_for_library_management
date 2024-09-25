from django.contrib import admin

from relbooks.models import RelBook


@admin.register(RelBook)
class ReLBookAdmin(admin.ModelAdmin):
    list_display = ("id", "book", "user", "release_date", "return_date")
    ordering = ["id"]
