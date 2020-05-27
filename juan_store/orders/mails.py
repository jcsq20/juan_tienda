from django.conf import settings

from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives

class Mail:
    @staticmethod
    def send_complete_order(order, user):
        subject = "tu pedido ha sido enviado" #mensaje asunto correo 
        template = get_template("orders/mails/complete.html") #template a redirigir
        content = template.render({#contexto
            "user": user,
            "order":order

        })

        message = EmailMultiAlternatives(subject,
                                            "Mensaje importante",#marca el mensaje como importante
                                            settings.EMAIL_HOST_USER,#de 
                                            [user.email])#para
        
        message.attach_alternative(content, "text/html")#configurar contenido como text/html
        message.send()#enviar