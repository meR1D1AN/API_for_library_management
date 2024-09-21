from django.contrib import admin

from relbooks.models import RelBook


@admin.register(RelBook)
class ReLBookAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'release_date', 'return_date')
