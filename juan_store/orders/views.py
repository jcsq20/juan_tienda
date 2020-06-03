import threading #para poner en segundo plano

from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages
from django.contrib.auth.decorators import login_required #funciona para redireccionar cuando un usuario no esta auntenticado
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.list import ListView

from django.db.models.query import EmptyQuerySet

from .models import Order
from shipping_addresess.models import ShippingAddress

from carts.utils import get_or_create_cart, destroy_cart
from .utils import get_or_create_order, breadcrumb, destroy_order

#decoradores
from .decorators import validate_cart_and_order

#correo
from .mails import Mail
# Create your views here.
#le dice a django que debe estar autenticado LoginRequiredMixin
class OrderListView(LoginRequiredMixin, ListView):
    login_url = "login"
    template_name = "orders/orders.html"

    def get_queryset(self):
        return self.request.user.orders_completed()

#le dice a django que el usuario debe estar autenticado y si no lo redirecciona a la direccion del parametro
@login_required(login_url="login")
@validate_cart_and_order
def order(request, cart, order):
    return render(request, 'orders/order.html', {
        "cart": cart,
        'order' : order,
        "breadcrumb": breadcrumb(),
    })

@login_required(login_url="login")
@validate_cart_and_order
def address(request, cart, order):
    shipping_address = order.get_or_set_shipping_address()
    can_choose_address = request.user.shippingaddress_set.count() > 1

    return render(request, "orders/address.html",{
        "cart": cart,
        "order": order,
        "shipping_addresses":shipping_address, 
        "breadcrumb":breadcrumb(address=True),
        "can_choose_address" : can_choose_address,
    })

@login_required(login_url="login")
def select_address(request):
    shipping_addresses = request.user.shippingaddress_set.all()
    return render(request, "orders/select_address.html",{
        "breadcrumb": breadcrumb(address=True),
        "shipping_addresses": shipping_addresses,

    })

@login_required(login_url="login")
@validate_cart_and_order
def check_address(request, cart, order, pk):
    shipping_address = get_object_or_404(ShippingAddress, pk=pk)

    if request.user.id != shipping_address.user_id:
        return redirect("carts:cart")

    order.update_shipping_address(shipping_address)
    return redirect("orders:address")

@login_required(login_url="login")
@validate_cart_and_order
def confirm(request, cart, order):
    shipping_address = order.shipping_address
    
    if shipping_address is None:
        return redirect("orders:address")
    return render(request, "orders/confirm.html", {
        "cart":cart,
        "order":order,
        "breadcrumb":breadcrumb(address=True, confirmation=True),
        "shipping_address":shipping_address,
    })

@login_required(login_url="login")
@validate_cart_and_order
def cancel(request,cart, order):
    
    if request.user.id != order.user_id:
        return redirect("carts:cart")

    order.cancel()

    destroy_cart(request)
    destroy_order(request)

    messages.error(request, "ordern cancelada")
    return redirect("index")

@login_required(login_url="login")
@validate_cart_and_order
def complete(request, cart, order):

    if request.user.id != order.user_id:
        return redirect("carts:cart")

    order.complete()

    thread = threading.Thread(target=Mail.send_complete_order, args=(
        order, request.user
    ))#target = metodo que se va ejecutar en segundo plano, args = argumentos del metodo 
    thread.start()#iniciar el thread

    destroy_cart(request)
    destroy_order(request)

    messages.success(request, "compra completada exitosamente")

    return redirect("index")