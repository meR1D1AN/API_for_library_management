from rest_framework import serializers

from authors.models import Author
from authors.serializers import AuthorSerializer
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(),
        source='author',
        write_only=True
    )

    class Meta:
        model = Book
        fields = "__all__"


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title']
