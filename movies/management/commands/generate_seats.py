from django.core.management.base import BaseCommand
from movies.models import CinemaHall, Seat


class Command(BaseCommand):
    help = 'Generates seats for all Cinema Halls'

    def handle(self, *args, **kwargs):
        halls = CinemaHall.objects.all()

        if not halls.exists():
            self.stdout.write(self.style.ERROR("No Cinema Halls found! Create a Hall in Admin first."))
            return

        for hall in halls:
            self.stdout.write(f"Generating seats for: {hall.name}...")

            seats_created = 0

            rows = ['A', 'B', 'C', 'D', 'E']

            seats_per_row = 10

            for row in rows:
                for number in range(1, seats_per_row + 1):

                    seat, created = Seat.objects.get_or_create(
                        hall=hall,
                        row_number=row,
                        seat_number=str(number)
                    )
                    if created:
                        seats_created += 1

            self.stdout.write(self.style.SUCCESS(f"  - Created {seats_created} seats for {hall.name}"))

        self.stdout.write(self.style.SUCCESS("All done!"))