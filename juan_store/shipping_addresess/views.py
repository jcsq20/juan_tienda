from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from .models import ShippingAddress
from .forms import ShippingAddressForm
# Create your views here.
class shippingAddressListView(LoginRequiredMixin, ListView):
    login_url = "login"
    model = ShippingAddress
    template_name = "shipping_addresses/shipping_addresses.html"

    def get_queryset(self):
        return ShippingAddress.objects.filter(user=self.request.user).order_by("-default")
#LoginRequired= asegura que el usuario este autenticado, SuccessM..=arroja un mensaje, Update=hereda la info para mostrar
class shippingAddressUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = "login"
    model = ShippingAddress
    form_class = ShippingAddressForm
    template_name = "shipping_addresses/update.html"
    success_message = "Direccion actualizada exitosamente"

    def get_success_url(self):
        return reverse("shipping_addresses:shipping_addresses")
    #permite generar validaciones sobre la peticion
    def dispatch(self, request, *args, **kwargs):
        if request.user.id != self.get_object().user_id:
            return redirect("carts:cart")
        return super(shippingAddressUpdateView, self).dispatch(request, *args, **kwargs)

@login_required(login_url="login")
def create(request):
    form = ShippingAddressForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        shipping_address = form.save(commit=False)
        shipping_address.user = request.user
        shipping_address.default = not ShippingAddress.objects.filter(user=request.user).exists()
        shipping_address.save()

        messages.success(request, "Direccion creada exitosamente")
        return redirect("shipping_addresses:shipping_addresses")

    return render(request,"shipping_addresses/create.html",{
        #contexto
        "form": form,
    })
