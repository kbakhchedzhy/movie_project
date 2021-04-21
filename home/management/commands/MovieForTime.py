import uuid
from datetime import date

from django.core.management.base import BaseCommand
from tmdbv3api import Discover, Movie

from home.models import MovieDetails, Genres, ProductionCompany, SpokenLanguage


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
                movie_db = MovieDetails()
                movie_details = movie.details(movie_id=this_movie.id)
                movie_db.backdrop_path = movie_details.backdrop_path
                movie_db.budget = movie_details.budget
                movie_db.id = movie_details.id
                movie_db.imdb_id = movie_details.imdb_id
                movie_db.original_language = movie_details.original_language
                movie_db.original_title = movie_details.original_title
                movie_db.overview = movie_details.overview
                movie_db.popularity = movie_details.popularity
                movie_db.poster_path = movie_details.poster_path
                movie_db.release_date = movie_details.release_date
                movie_db.revenue = movie_details.revenue
                movie_db.runtime = movie_details.runtime# movie_db.spoken_languages = movie_details.spoken_languages
                movie_db.status = movie_details.status
                movie_db.tagline = movie_details.tagline
                movie_db.title = movie_details.title
                movie_db.video = movie_details.video
                movie_db.vote_average = movie_details.vote_average
                movie_db.vote_count = movie_details.vote_count

                movie_db.save()

                for one_of_genres in movie_details.genres:
                    genre, _ = Genres.objects.get_or_create(
                        id=one_of_genres.id,
                        title=one_of_genres.name)
                    movie_db.genres.add(genre)

                for one_of_prodcompany in movie_details.production_companies:
                    prodcompany, _ = ProductionCompany.objects.get_or_create(
                        id=one_of_prodcompany.id,
                        name=one_of_prodcompany.name,
                        logo_path=one_of_prodcompany.logo_path,
                        origin_country=one_of_prodcompany.origin_country)
                    movie_db.production_companies.add(prodcompany)

                for one_of_sp_language in movie_details.spoken_languages:
                    sp_language, _ = SpokenLanguage.objects.get_or_create(
                        iso_639_1=one_of_sp_language.iso_639_1,
                        name=one_of_sp_language.name)
                    movie_db.spoken_languages.add(sp_language)

            self.stdout.write('Finished\n')

        else:
            self.stdout.write('Please, enter period of time.')
