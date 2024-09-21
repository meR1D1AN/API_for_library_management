from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = 'Создание учётки админа'

    def handle(self, *args, **options):
        user = User.objects.create(
            first_name='Admin',
            last_name='Adminov',
            email='admin@admin.ru',
            is_superuser=True,
            is_staff=True,
            is_active=True,
            date_of_birth='1991-05-19',
            phone='+79992345678',
            bio="Скромно, но я админ"

        )
        user.set_password('qwe123')
        user.save()
