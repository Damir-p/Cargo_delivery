from django.apps import AppConfig
# from location.management.commands import load_locations

class LocationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'location'

    # def ready(self):
    #     post_migrate.connect(load_locations.Command().handle, sender=self)
