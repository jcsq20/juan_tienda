from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
from . import views

from productos.views import ProductoListView

urlpatterns = [#registrar las vistas 
    path("", ProductoListView.as_view(), name="index"),
    path("usuarios/login", views.login_view, name="login"),
    path("usuarios/registro", views.registro, name="registro"),
    path("usuarios/logout", views.logout_view, name="logout"),
    path('admin/', admin.site.urls),
    path("productos/", include("productos.urls")),
    path("carrito/", include("carts.urls")),
    path("orden/", include("orders.urls")),
    path("direcciones/", include("shipping_addresess.urls")),
    path("codigos/", include("promo_codes.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)