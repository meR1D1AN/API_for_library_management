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
        queryset=Book.objects.all(), source="book", write_only=True
    )
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="user", write_only=True
    )

    class Meta:
        model = RelBook
        fields = [
            "id",
            "release_date",
            "book_id",
            "book",
            "user_id",
            "user",
            "return_date",
        ]


class RelBookCreateSerializer(RelBookSerializer):

    class Meta(RelBookSerializer.Meta):
        fields = ["release_date", "book_id", "user_id"]
