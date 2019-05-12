
from ..models import Airline, City, Ticket

from rest_framework.serializers import ModelSerializer


class AirlineSerializer(ModelSerializer):

    class Meta:
        model = Airline
        fields = [
            'id',
            'name'
        ]


class CitySerializer(ModelSerializer):

    class Meta:
        model = City
        fields = [
            'id',
            'name',
            'country'
        ]


class TicketSerializer(ModelSerializer):
    airline = AirlineSerializer()
    start_city = CitySerializer()
    end_city = CitySerializer()

    class Meta:
        model = Ticket
        fields = [
            'id',
            'start_city',
            'end_city',
            'description',
            'airline',
            'start_date',
            'end_date',
            'url_detail',
        ]
