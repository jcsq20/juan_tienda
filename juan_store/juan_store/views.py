from django.shortcuts import render, redirect #render(renderisar un template) y redirect(redireccionar)

from django.contrib.auth import login #generar la session
from django.contrib.auth import logout # cerrar la session
from django.contrib import messages# mensajes de alerta
from django.contrib.auth import authenticate #verificar el usuario

#from django.contrib.auth.models import User
from users.models import User

from productos.models import Producto
from .forms import RegisterForm #llamar los formularios

def index(request):
    productos = Producto.objects.all().order_by("-id")
    return render(request,"index.html",{#este recibe 3 argumentos la peticion, la ruta y el contexto
        #context
        'mesage': 'Listado de productos',
        "titulo": "Productos",
        "productos": productos,
    })

def login_view(request):
    if request.user.is_authenticated:
        return redirect("index")
    if request.method == "POST":
        username = request.POST.get("username")
        pasword = request.POST.get("password")
        user = authenticate(username=username, password=pasword)#funcion django para corroborar que exista el usuario
        if user:
            login(request, user)
            messages.success(request,"Bienvenido %s" %user.username)
            #messages.success(request,"Bienvenido {}" . format(user.username))
            return redirect("index")# envia si el formulario esta correcto a index
        else:
            messages.error(request,"Usuario o contraseña no validos")

    return render(request, "usuarios/login.html",{


    })

def logout_view(request):
    logout(request)
    messages.success(request,"Sesion cerrada exitosamente")
    return redirect("login")

def registro(request):
    if request.user.is_authenticated:
        return redirect(index)
    #obtener la informacion mediante la clase forms
    form = RegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        if user:
            login(request, user)
            messages.success(request,"Usuario creado con exito")
            return redirect("index")
    return render(request,"usuarios/registro.html",{
        "form": form
    })