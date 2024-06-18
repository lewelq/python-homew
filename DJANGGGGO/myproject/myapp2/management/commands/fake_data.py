from django.core.management.base import BaseCommand
from myapp2.models import Author, Post

class Command(BaseCommand):
    help = 'update.'

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(name=f'Name{i}', email=f'mail{i}@mail.fds')
            author.save()
            for j in range(1, count + 1):
                post = Post(
                    title=f'Title{j}',
                    content=f'Text from {author.name} #{j} example',
                    author=author
                )
                post.save()
