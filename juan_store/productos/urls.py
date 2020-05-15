from django.urls import path
from . import views


app_name= "productos"

urlpatterns = [#registrar las vistas 
    path("search",views.ProductoSearchListView.as_view(),name="search"),
    path("<slug:slug>",views.ProductoDetailView.as_view(), name="producto") #<nombre_atributo:tipo_atributo>
    
]
