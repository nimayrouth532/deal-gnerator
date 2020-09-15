from django.urls import path
from . import views
urlpatterns = [
    path("amazon/", views.amazon),
    path("amazon/deals-generated/", views.nimaydeals),
]
