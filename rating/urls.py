from django.urls import path
from . import views

app_name = "rating"

urlpatterns = [
    path("add/<int:product_id>/", views.add_rating, name="add_rating"),
]
