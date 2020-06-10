from . import stripe

def create_charge(order):
    if order.billing_profile and order.user and order.user.customer_id:
        charge = stripe.Charge.create(
            amount = int(order.total)*100, #centavos
            currency ="USD", #moneda
            description = order.description, #descripcion 
            customer = order.user.customer_id,#aquien se le hace el cobro
            source = order.billing_profile.card_id, #metodo de pago
            metadata={
                "order_id":order.id
            }
        )
        return charge