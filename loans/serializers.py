from rest_framework import serializers

from books.models import Book
from users.models import User
from .models import Loan
from books.serializers import BookSerializer
from users.serializers import UserSerializer


class LoanSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    user = UserSerializer(read_only=True)
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
        model = Loan
        fields = ['id', 'book', 'book_id', 'user', 'user_id', 'loan_date', 'return_date']
