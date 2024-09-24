from rest_framework import serializers

from books.models import Book
from users.models import User
from .models import RelBook
from books.serializers import BookListSerializer
from users.serializers import UserListSerializer


class RelBookSerializer(serializers.ModelSerializer):
    book = BookListSerializer(read_only=True)
    user = UserListSerializer(read_only=True)
    book_id = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all(),
        source='book',
        write_only=True
    )
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='user',
        write_only=True
    )

    class Meta:
        model = RelBook
        fields = ['id', 'release_date', 'book', 'book_id', 'user', 'user_id', 'return_date']
