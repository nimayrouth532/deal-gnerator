from django.urls import path
from . import views

urlpatterns = [
   path("flipkart/", views.flip),
   path("flipkart/deals/", views.deals),
]
