from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from products.models import Product
from django.http import HttpResponse


@login_required




def place_order(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        payment_method = request.POST.get("payment_method", "COD")

        product = get_object_or_404(Product, id=product_id)

        # Calculate price
        price = product.discount_price or product.price

        # Create order
        order = Order.objects.create(
            user=request.user,
            product=product,
            quantity=1,
            total_amount=price,
            payment_method=payment_method
        )

        return redirect("orders:order_success", order_id=order.id)

    return redirect("home")





@login_required
def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, "orders/order_success.html", {"order": order})
@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "orders/my_orders.html", {"orders": orders})
@login_required
def order_summary(request):
    return render(request, "orders/order_summary.html")
def online_payment(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    # Temporary: simulate online payment success
    order.is_paid = True
    order.save()

    return redirect("orders:order_success", order_id=order.id)
def checkout(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        product = get_object_or_404(Product, id=product_id)

        return render(request, "orders/checkout.html", {
            "product": product
        })

    return redirect("home")
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})