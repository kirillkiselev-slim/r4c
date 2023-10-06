from django.urls import path
from .views import create_robot, download_excel_report


APP_NAME = "robots"
urlpatterns = [
    path("robots", create_robot, name="create-robot"),
    path("robots/excel-report", download_excel_report, name="download-robot-report")
]
