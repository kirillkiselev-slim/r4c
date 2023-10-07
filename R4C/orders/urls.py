from django.urls import path
from .views import check_availability


APP_NAME = "orders"
urlpatterns = [
    path("order", check_availability, name="order")
]