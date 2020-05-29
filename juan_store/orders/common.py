# se crea para evitar errores debido a models.py orders y models.py carts lo llaman
from enum import Enum
class OrderStatus(Enum):
    CREATED = "CREATED" #creado
    PAYED = "PAYED" #pagado
    COMPLETED = "COMPLETED" #completado
    CANCELED = "CANCELED" #cancelado

choices = [ (tag, tag.value) for tag in OrderStatus ]