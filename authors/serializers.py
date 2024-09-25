from rest_framework import serializers
from .models import Author
from books.book_serializers import BookListSerializer


class AuthorSerializer(serializers.ModelSerializer):
    books = BookListSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["id", "name", "bio", "date_of_birth", "books"]
