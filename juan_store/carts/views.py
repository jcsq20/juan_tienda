from django.shortcuts import render
from .utils import get_or_create_cart
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

    })