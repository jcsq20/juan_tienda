from django.contrib import admin
from .models import PromoCode

class PromoCodeAdmin(admin.ModelAdmin):
    exclude = ["code"]
# Register your models here.
admin.site.register(PromoCode, PromoCodeAdmin)