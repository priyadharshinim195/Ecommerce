from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path('', views.product_list, name='product_list'),
 # Wishlist URLs inside products app
    path('wishlist/', views.wishlist_page, name='wishlist_page'),
    path('wishlist/add/<slug:slug>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<slug:slug>/', views.remove_from_wishlist, name='remove_from_wishlist'),

    path('category/<slug:slug>/', views.category_products, name='category_products'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
    
     # leave this last
]