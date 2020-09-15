from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("Homepage.urls")),
    path("", include("flipkart.urls")),
    path("", include("amazon.urls")),
]