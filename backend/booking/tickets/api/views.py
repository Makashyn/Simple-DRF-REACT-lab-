
from ..models import Airline, City, Ticket


from .serializers import TicketSerializer

from .pagination import PostPageNumberPagination
from rest_framework.viewsets import ReadOnlyModelViewSet


class TicketsViewSet(ReadOnlyModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    search_fields = ['airline__name', 'description', 'start_date', 'end_date', 'start_city__name', 'end_city__name']
    filter_fields = ['id', 'airline', 'start_date', 'end_date', 'start_city', 'end_city']
    pagination_class = PostPageNumberPagination