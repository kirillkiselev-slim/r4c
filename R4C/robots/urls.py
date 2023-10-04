from django.urls import path
from .views import create_robot


APP_NAME = "robots"
urlpatterns = [
    path("robots/", create_robot, name="create-robot"),
]
