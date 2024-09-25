from rest_framework import serializers
from books.models import Book
from authors.models import Author
from authors.serializers import AuthorListSerializer


class BookSerializer(serializers.ModelSerializer):
    author = AuthorListSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), source="author", write_only=True
    )

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "author_id",
            "genre",
            "description",
            "published_date",
            "isbn",
            "count",
        ]


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title"]
