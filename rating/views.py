from django.shortcuts import render, redirect, get_object_or_404
from .models import Rating
from products.models import Product
from django.contrib.auth.decorators import login_required

@login_required
def add_rating(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        print("Form submitted", request.POST)  # 🔥 check POST data comes or not
        
        stars = request.POST.get("stars")
        review = request.POST.get("review")

        Rating.objects.update_or_create(
            user=request.user,
            product=product,
            defaults={"stars": stars, "review": review}
        )

    return redirect("products:product_detail", slug=product.slug)

