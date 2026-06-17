from django.apps import AppConfig
from django.conf import settings


class StafflaneMeetConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "stafflane_meet"
    verbose_name = "Stafflane Meet"

    def ready(self):
        from django.urls import include, path

        from stafflane.urls import urlpatterns
        from stafflane_meet import signals

        settings.APPS.append("stafflane_meet")

        urlpatterns.append(
            path("meet/", include("stafflane_meet.urls")),
        )
        super().ready()
