from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Avg
from django.http import Http404
from django.contrib import messages

from .models import Product, Review, Category
from wishlist.models import Wishlist
from rating.models import Rating


# -----------------------------------------
# PRODUCT LIST
# -----------------------------------------
def product_list(request):
    q = request.GET.get('search', '')
    category_id = request.GET.get('category', '')

    products = Product.objects.filter(is_active=True).order_by('-created_at')

    if q:
        products = products.filter(name__icontains=q)

    if category_id:
        products = products.filter(category_id=category_id)

    paginator = Paginator(products, 8)
    page_obj = paginator.get_page(request.GET.get('page'))

    categories = Category.objects.all()

    return render(request, 'products/product_list.html', {
        'page_obj': page_obj,
        'categories': categories,
        'search_query': q,
        'selected_category': category_id,
    })


# -----------------------------------------
# PRODUCT DETAIL PAGE (FINAL CORRECT VERSION)
# -----------------------------------------
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)

    # Wishlist check
    item_in_wishlist = False
    if request.user.is_authenticated:
        item_in_wishlist = Wishlist.objects.filter(user=request.user, product=product).exists()

    # Discount calculation
    discount = None
    if product.price and product.discount_price:
        discount = round((product.price - product.discount_price) / product.price * 100)

    return render(request, 'products/product_detail.html', {
        'product': product,
        'item_in_wishlist': item_in_wishlist,
        'discount': discount,
    })


# -----------------------------------------
# CATEGORY PRODUCTS
# -----------------------------------------
def category_products(request, slug):
    category = Category.objects.filter(slug=slug).first()

    if not category:
        category = Category.objects.filter(slug__icontains=slug).first()

    if not category:
        raise Http404("Category not found")

    products = Product.objects.filter(category=category, is_active=True)

    return render(request, "products/category_products.html", {
        "category": category,
        "products": products
    })


# -----------------------------------------
# WISHLIST (ONLY 1 CLEAN VERSION)
# -----------------------------------------
@login_required
def add_to_wishlist(request, slug):
    product = get_object_or_404(Product, slug=slug)
    Wishlist.objects.get_or_create(user=request.user, product=product)
    messages.success(request, "Added to wishlist ❤️")
    return redirect(request.META.get("HTTP_REFERER", "/"))


@login_required
def remove_from_wishlist(request, slug):
    product = get_object_or_404(Product, slug=slug)
    Wishlist.objects.filter(user=request.user, product=product).delete()
    return redirect(request.META.get("HTTP_REFERER", "/"))


@login_required
def wishlist_page(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, "products/wishlist.html", {
        "wishlist_items": wishlist_items
    })


# -----------------------------------------
# SEARCH
# -----------------------------------------
def search_products(request):
    query = request.GET.get("q", "")
    category = request.GET.get("category", "")
    brand = request.GET.get("brand", "")
    min_price = request.GET.get("min_price", "")
    max_price = request.GET.get("max_price", "")

    products = Product.objects.all()

    if query:
        products = products.filter(name__icontains=query)

    if category:
        products = products.filter(category__slug=category)

    if brand:
        products = products.filter(brand__icontains=brand)

    if min_price:
        products = products.filter(price__gte=min_price)

    if max_price:
        products = products.filter(price__lte=max_price)

    categories = Category.objects.all()
    brands = Product.objects.values_list("brand", flat=True).distinct()

    return render(request, "products/search_results.html", {
        "results": products,
        "query": query,
        "categories": categories,
        "brands": brands,
    })
