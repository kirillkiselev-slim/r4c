from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", include("customers.urls")),
    path("", include("orders.urls")),
    path("", include("robots.urls"))
]