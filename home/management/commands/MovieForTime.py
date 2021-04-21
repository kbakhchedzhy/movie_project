import uuid
from datetime import date

from django.core.management.base import BaseCommand
from tmdbv3api import Discover, Movie


class Command(BaseCommand):

    help = 'Add movies for some time. Choose period of time' # noqa

    def add_arguments(self, parser):
        parser.add_argument('-b', '--begin', type=str, default='1874-12-09')
        parser.add_argument('-e', '--end', type=str, default=date.today())

    def handle(self, *args, **options):

        if options['begin'] or options['end']:

            dis = Discover()
            movie = Movie()
            all_movies = dis.discover_movies(params={'release_date.gte': options['begin'], 'release_date.lte': options['end']})
            for this_movie in all_movies:
                print(movie.details(movie_id=this_movie.id))
            print("\n\n\n")

        else:
            self.stdout.write('Please, enter period of time.')
