from django.apps import AppConfig


class KiteApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "kite_api"

    def ready(self):
        from django.urls import include, path

        from kite.urls import urlpatterns

        urlpatterns.append(
            path("api/", include("kite_api.urls")),
        )
        super().ready()
