from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Print helllo world'

    def handle(self, *args, **kwargs):
        self.stdout.write('hello world')