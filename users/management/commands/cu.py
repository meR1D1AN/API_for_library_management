from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    help = "Создание тестовой учётки"

    def handle(self, *args, **options):
        user = User.objects.create(
            first_name="Test",
            last_name="Testov",
            email="test@test.ru",
            is_superuser=False,
            is_staff=False,
            is_active=True,
            date_of_birth="1991-05-19",
            phone="+79991234567",
            bio="Тестовая учётка",
        )
        user.set_password("qwe123")
        user.save()
