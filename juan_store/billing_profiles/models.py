from django.db import models
from users.models import User
# Create your models here.
class BillingProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #para tarjetas debido o credito / no almacenaremos datos de facturacion eso lo hace strike
    # esos 4 atributos los obtendremos de strike
    token = models.CharField(max_length=50,null=False, blank=False) # 
    card_id = models.CharField(max_length=50,null=False, blank=False)#
    last4 = models.CharField(max_length=4,null=False, blank=False)# ultims 4 dijitos tarjeta
    brand = models.CharField(max_length=10,null=False, blank=False) # marca tarjeta (Visa, Mastercard)
    default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.card_id