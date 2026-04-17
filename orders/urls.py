from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    # path("checkout/<int:product_id>/", views.checkout, name="checkout"),
    path("place/", views.place_order, name="place_order"),
    path('my-orders/', views.my_orders, name='my_orders'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path("success/<int:order_id>/", views.order_success, name="order_success"),
    path("summary/", views.order_summary, name="order_summary"),
    path("pay/<int:order_id>/", views.online_payment, name="online_payment"),
    path("checkout/", views.checkout, name="checkout"),


]
