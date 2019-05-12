from django.urls import path
from .views import (
    TicketsViewSet,
)
#
from rest_framework.routers import SimpleRouter

app_name = 'tickets-api'

router = SimpleRouter()

router.register(r'tickets', TicketsViewSet)

urlpatterns = router.urls