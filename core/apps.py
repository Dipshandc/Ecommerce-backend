from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'



    def ready(self):
        from .singnals.handlers import create_customer , save_customer

        from django.contrib.auth.models import User
        from django.db.models.signals import post_save
        post_save.connect(create_customer, sender=User)
        post_save.connect(save_customer, sender=User)
