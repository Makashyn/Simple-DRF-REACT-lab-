from django.test import TestCase

# Create your tests here.

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Ticket, City, Airline


class TicketTests(APITestCase):

    def setUp(self) -> None:
        ''' Create one record in db
        '''

        City.objects.create(name='Kyiv', country='Ukraine', timestamp='2019-06-13 20:04:57.440')
        City.objects.create(name='Berlin', country='Germany', timestamp='2019-06-13 20:04:57.440')

        Airline.objects.create(name='Turkish airlines', timestamp='2019-06-13 20:04:57.440')


        Ticket.objects.create(start_city_id=1, end_city_id=2, description='Something', airline_id=1,
            start_date='2019-06-13 20:04:57.440', end_date='2019-06-13 20:04:57.440',
            timestamp='2019-06-13 20:04:57.440', price=100.00)



    def test_list_api(self):
        ''' Ensure that we get correct ticket list data
        '''

        url = reverse('tickets-api:ticket-list')
        responce = self.client.get(url)
        self.assertEqual(responce.status_code, status.HTTP_200_OK)
        self.assertEqual(len(responce.data), 4)

    def test_detail_api(self):
        ''' Ensure that we get correct ticket detail data
        '''
        ticket_id = Ticket.objects.all().first().id
        url = reverse('tickets-api:ticket-detail', args=(ticket_id, ))
        responce = self.client.get(url)
        self.assertEqual(responce.status_code, status.HTTP_200_OK)


    def test_db_create(self):
        ''' Ensure that we can create new record in db
        '''

        City.objects.create(name='New-York', country='USA', timestamp='2019-06-13 20:04:57.440')

        Airline.objects.create(name='Turkish airlines', timestamp='2019-06-13 20:04:57.440')


        Ticket.objects.create(start_city_id=2, end_city_id=3, description='Something', airline_id=1,
            start_date='2019-06-13 20:04:57.440', end_date='2019-06-13 20:04:57.440',
            timestamp='2019-06-13 20:04:57.440', price=100.00)

        self.assertEqual(Ticket.objects.get(id=2).start_city_id, 2)
        self.assertEqual(Ticket.objects.get(id=2).end_city_id, 3)
        self.assertEqual(Ticket.objects.get(id=2).price, 100.00)
