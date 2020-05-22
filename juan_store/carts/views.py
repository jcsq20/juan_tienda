from django.shortcuts import render, redirect, get_object_or_404
from .utils import get_or_create_cart
from productos.models import Producto
from .models import CartProductos

# Create your views here.

def cart(request):
    #request.session["cart_id"] = None
    cart = get_or_create_cart(request)

    #crear una session
    #request.session["cart_id"]= "123"#diccionario

    #obtendremos el valor de una session
    #valor = request.session.get("cart_id")
    #print(valor)
    #eliminar una session
    #request.session["cart_id"] = None
    return render(request, "carts/cart.html", {
        "cart":cart
    })

def add(request):
    cart = get_or_create_cart(request)
    producto = get_object_or_404(Producto, pk=request.POST.get("product_id"))#asegurar que muestre el error 404 quiere decir que no es usado un recurso
    quantity= int(request.POST.get("quantity", 1)) #por el servidor recibe por name del formulario
    print(quantity)
    #producto = Producto.objects.get(pk=request.POST.get("product_id"))

    #cart.productos.add(producto, through_defaults={ 
     #   'quantity': quantity
    #})#aprovechando la relacion agregamos un objecto a esta misma
    cart_producto = CartProductos.objects.create_or_update_quantity(cart=cart, producto=producto, quantity=quantity)

    return render(request, "carts/add.html", {
        'quantity': quantity,
        'cart_producto' : cart_producto,
        "producto" : producto
    })

def remove(request):
    cart = get_or_create_cart(request)
    #asegurar que muestre el error 404 quiere decir que no es usado un recurso
    producto = get_object_or_404(Producto, pk=request.POST.get("product_id"))
    cart.productos.remove(producto)

    return redirect("carts:cart")