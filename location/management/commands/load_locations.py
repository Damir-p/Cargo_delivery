import csv
from django.core.management.base import BaseCommand
from location.models import Location

class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('uszips.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                location = Location(
                    city=row['city'],
                    state=row['state_name'],
                    zipcode=row['zip'],
                    latitude=row['lat'],
                    longitude=row['lng']
                )
                location.save()
        self.stdout.write(self.style.SUCCESS('Локации успешно загружены'))

