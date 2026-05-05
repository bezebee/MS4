from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'
    label = 'store_checkout'
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        import checkout.signals
