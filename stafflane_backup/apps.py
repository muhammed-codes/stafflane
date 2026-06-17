from django.apps import AppConfig


class BackupConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "stafflane_backup"

    def ready(self):
        from django.urls import include, path

        from stafflane.urls import urlpatterns

        urlpatterns.append(
            path("backup/", include("stafflane_backup.urls")),
        )
        super().ready()
