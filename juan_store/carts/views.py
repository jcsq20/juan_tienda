from django.shortcuts import render
from .models import Cart
# Create your views here.

def cart(request):
    #request.session["cart_id"] = None
    user = request.user if request.user.is_authenticated else None #obtenemos usuario autenticado
    cart_id = request.session.get("cart_id")
    if cart_id:
        cart = Cart.objects.get(cart_id=cart_id)
    else:
        cart = Cart.objects.create(user=user)
    request.session["cart_id"] = cart.cart_id

    #crear una session
    #request.session["cart_id"]= "123"#diccionario

    #obtendremos el valor de una session
    #valor = request.session.get("cart_id")
    #print(valor)
    #eliminar una session
    #request.session["cart_id"] = None
    return render(request, "carts/cart.html", {

    })