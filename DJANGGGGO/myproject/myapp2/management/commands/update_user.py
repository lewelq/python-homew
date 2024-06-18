from django.core.management.base import BaseCommand
from myapp2.models import User

class Command(BaseCommand):
    help = 'update.'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='user id')
        parser.add_argument('name', type=str, help='username')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        user = User.objects.filter(pk=pk).first()
        user.name = name
        user.save()
        self.stdout.write(f'{user}')
        