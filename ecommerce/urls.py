"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include,path
from django.contrib import admin
from cart import views as cart_views
from products import views as product_views
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path("", include("landing.urls")),
    path("deals/", include("deals.urls")),  # ⭐ This enables /deals/ and /products/
    path('products/', include('products.urls')),
    path("cart/", include("cart.urls")),
    path("orders/", include("orders.urls")),
    path("accounts/", include("accounts.urls")),
    path("admin/", admin.site.urls),
    path('wishlist/', include('wishlist.urls', namespace='wishlist')),


    path('search/', product_views.search_products, name='search'),
    path('rating/', include('rating.urls')),

]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
