from rest_framework import serializers
from .models import Book
from authors.models import Author


class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = ["id", "title", "author"]


class BookShotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title"]
