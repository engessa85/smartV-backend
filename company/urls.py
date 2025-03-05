from django.urls import path
from .views import CompanyListCreateAPIView


urlpatterns = [
   path('companies/', CompanyListCreateAPIView.as_view(), name='company-list-create'),
]
