from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'the_foodhub.accounts'

    def ready(self):
        import the_foodhub.accounts.signals