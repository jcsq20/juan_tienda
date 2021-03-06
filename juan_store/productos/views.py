from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.db.models import Q
from .models import Producto
# Create your views here.
class ProductoListView(ListView):
    template_name = "index.html"
    queryset = Producto.objects.all().order_by("-id")
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mesage"] = "Listado de productos"
        return context

class ProductoDetailView(DetailView):
    model = Producto
    template_name = "productos/producto.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context

class ProductoSearchListView(ListView):
    template_name = "productos/search.html"
    
    def get_queryset(self):
        #filters = Q(titulo__icontains=self.query() | Q(category__titulo__icontains=self.query()))
        filters = Q(categoria__titulo__icontains=self.query()) |Q(titulo__icontains=self.query())
        return Producto.objects.filter(filters)

    def query(self):
        return self.request.GET.get("q")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()
        context["count"] = context["producto_list"].count()
        return context
