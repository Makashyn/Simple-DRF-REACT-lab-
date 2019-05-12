from django.contrib import admin
from .models import Ticket, City, Airline
# Register your models here.


admin.site.register(Ticket)
admin.site.register(City)
admin.site.register(Airline)

