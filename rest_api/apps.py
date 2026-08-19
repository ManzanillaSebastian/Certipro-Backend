from django.apps import AppConfig


class RestApiConfig(AppConfig):
    name = "rest_api"

    def ready(self):
        from . import signals  # noqa: F401
