from stripeAPI.card import create_card

from django.db import models
from users.models import User
# Create your models here.
class BillingProfileManager(models.Manager):
    def create_by_stripe_token(self, user, stripe_token):
        if user.has_customer() and stripe_token:
            source = create_card(user, stripe_token)

            return self.create(card_id=source.id,
                                last4=source.last4,
                                token=stripe_token,
                                brand=source.brand,
                                user=user,
                                default= not user.has_billing_profiles())

class BillingProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #para tarjetas debido o credito / no almacenaremos datos de facturacion eso lo hace strike
    # esos 4 atributos los obtendremos de strike
    token = models.CharField(max_length=50,null=False, blank=False) # 
    card_id = models.CharField(max_length=100,null=False, blank=False)#
    last4 = models.CharField(max_length=4,null=False, blank=False)# ultims 4 dijitos tarjeta
    brand = models.CharField(max_length=10,null=False, blank=False) # marca tarjeta (Visa, Mastercard)
    default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = BillingProfileManager()
    
    def __str__(self):
        return self.card_id
