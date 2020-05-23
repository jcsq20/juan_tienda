from django.urls import path

from . import views

app_name = "shipping_addresses"

urlpatterns =[
    path("", views.shippingAddressListView.as_view(), name="shipping_addresses"),
    path("nuevo", views.create, name="create"),
    path("editar/<int:pk>", views.shippingAddressUpdateView.as_view(), name="update"),
    path("eliminar/<int:pk>", views.shippingAddressDeleteView.as_view(), name="delete"),
    path("default/<int:pk>", views.default, name="default"),
]