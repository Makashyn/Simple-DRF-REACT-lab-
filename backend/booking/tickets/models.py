from django.db import models
from django.urls import reverse
# Create your models here.


class Ticket(models.Model):
    start_city = models.ForeignKey('City', on_delete=models.CASCADE, related_name='+',
        help_text='Ticket start endpoint')
    end_city = models.ForeignKey('City', on_delete=models.CASCADE, related_name='+',
        help_text='Ticket end endpoint')
    description = models.TextField(null=True, blank=True, help_text='Description of the ticker')
    airline = models.ForeignKey('Airline', on_delete=models.CASCADE, related_name='+',
        help_text='Airline of the ticket')

    price = models.DecimalField(max_digits=10, help_text='Price of the ticket')

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return '{} - {}'.format(self.start_city, self.end_city)

    @property
    def url_detail(self):
        return reverse('tickets-api:ticket-detail', args=(self.pk, ))


class City(models.Model):
    name = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        unique_together = ('name', 'country', )

    def __str__(self):
        return self.name


class Airline(models.Model):
    name = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = 'Airline'
        verbose_name_plural = 'Airlines'

    def __str__(self):
        return self.name