from django.apps import AppConfig


class NullableAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'nullable'
