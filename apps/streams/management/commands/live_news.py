from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = (
        'Stream live news messages. DISABLED: the Satori real-time data '
        'service (satori-sdk-python) this relied on has been shut down.'
    )

    def handle(self, *args, **options):
        raise CommandError(
            "The 'newsapi' Satori channel is no longer available. "
            "Satori (open-data.api.satori.com) was discontinued; wire up a "
            "replacement pub/sub source before re-enabling this command."
        )
