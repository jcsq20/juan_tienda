import uuid
from enum import Enum
from django.db import models
from django.db.models.signals import pre_save

from users.models import User
from carts.models import Cart
# Create your models here.

class OrderStatus(Enum):
    CREATED = "CREATED" #creado
    PAYED = "PAYED" #pagado
    COMPLETED = "COMPLETED" #completado
    CANCELED = "CANCELED" #cancelado

choices = [ (tag, tag.value) for tag in OrderStatus ]

class Order(models.Model):
    order_id = models.CharField(max_length=100, null=False, blank=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=choices, default=OrderStatus.CREATED)
    shipping_total = models.DecimalField(default=5, max_digits=8, decimal_places=2)
    total = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_id

    def update_total(self):
        self.total = self.get_total()

    def get_total(self):
        return self.cart.total + self.shipping_total

#callback
def set_order_id(sender, instance, *args, **kwars):
    if not instance.order_id:
        instance.order_id = str(uuid.uuid4())

def set_total(sender, instance, *args, **kwars):
    instance.total = instance.get_total()
#signal antes de almacenar
pre_save.connect(set_order_id, sender=Order)
pre_save.connect(set_total, sender=Order)

