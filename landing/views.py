from django.shortcuts import render
from .models import Category, CarouselImage, Product
from django.shortcuts import redirect
from django.utils.text import slugify
from wishlist.models import Wishlist

def index(request):
    categories = Category.objects.all()

    top_deals = Product.objects.order_by('-id')[:8]
    trending = Product.objects.order_by('?')[:10]

    # ⭐ Wishlist IDs
    wishlist_ids = []
    if request.user.is_authenticated:
        wishlist_ids = list(
            Wishlist.objects.filter(user=request.user)
            .values_list("product_id", flat=True)
        )

    return render(request, "landing/index.html", {
        "categories": categories,
        "top_deals": top_deals,
        "trending": trending,
        "wishlist_ids": wishlist_ids,
    })

def orders_home(request):
    return redirect('orders:order_summary')
from products.models import Category

def home(request):
    categories = Category.objects.all()
    return render(request, "landing/index.html", {"categories": categories})







