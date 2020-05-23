from .models import Order
from django.urls import reverse
def get_or_create_order(cart, request):
    order = cart.order

    if order is None and request.user.is_authenticated:
        order = Order.objects.create(cart=cart, user=request.user)
    if order:
        request.session["order_id"] = order.order_id

    return order

def breadcrumb(productos=True, addres=False, payment=False, confirmation=False):
    return [
        {"titulo": "productos", "active": productos, "url": reverse("orders:order")},
        {"titulo": "Direccion", "active": addres, "url": reverse("orders:order")},
        {"titulo": "Pago", "active": payment, "url": reverse("orders:order")},
        {"titulo": "Confirmacion", "active": confirmation, "url": reverse("orders:order")},
    ]