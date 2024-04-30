from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'



    def ready(self):
        from .signals.handlers import create_customer , save_customer , product_added

        from django.contrib.auth.models import User
        from .models import Product
        from django.db.models.signals import post_save
        post_save.connect(create_customer, sender=User)
        post_save.connect(save_customer, sender=User)
        post_save.connect(product_added, sender=Product)

