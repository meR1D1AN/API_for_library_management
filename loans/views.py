from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from books.paginators import StandardResultsSetPagination
from .models import Loan
from .serializers import LoanSerializer


class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination
