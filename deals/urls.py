from django.urls import path
from . import views

app_name = 'deals'

urlpatterns = [
    path('', views.deals_list, name='deal_list'),       # List of deals
    path('<int:pk>/', views.deal_detail, name='deal_detail'),  # Single deal
]
