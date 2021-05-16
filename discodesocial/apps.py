from django.apps import AppConfig


class DiscodesocialConfig(AppConfig):
    name = 'discodesocial'

    def ready(self):
        import discodesocial.signals
