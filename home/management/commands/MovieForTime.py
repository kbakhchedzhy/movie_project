from datetime import date

from django.core.management.base import BaseCommand
from tmdbv3api import Discover, Movie, Person

from home.models import MovieDetails, Genres, \
    ProductionCompany, SpokenLanguage, People, Cast, Crew


class Command(BaseCommand):

    help = 'Add movies for some time. Choose period of time' # noqa

    def add_arguments(self, parser):
        parser.add_argument('-b', '--begin', type=str, default='1874-12-09')
        parser.add_argument('-e', '--end', type=str, default=date.today())

    def handle(self, *args, **options):

        discover_tmdb = Discover()
        movie_tmdb = Movie()
        person_tmdb = Person()

        page_count = 1

        while 1:
            all_discovered_movies = discover_tmdb.discover_movies(
                params={
                    'primary_release_date.gte': options['begin'],
                    'primary_release_date.lte': options['end'],
                    'page': page_count
                })
            if all_discovered_movies:

                # Create movie and its relations

                for this_discovered_movie in all_discovered_movies:

                    # Create main values of movie

                    movie_db = MovieDetails()
                    movie_details = movie_tmdb.details(
                        movie_id=this_discovered_movie.id
                    )
                    movie_db.backdrop_path = movie_details.backdrop_path
                    movie_db.budget = movie_details.budget
                    movie_db.id = movie_details.id
                    movie_db.imdb_id = movie_details.imdb_id
                    movie_db.original_language = \
                        movie_details.original_language
                    movie_db.original_title = movie_details.original_title
                    movie_db.overview = movie_details.overview
                    movie_db.popularity = movie_details.popularity
                    movie_db.poster_path = movie_details.poster_path
                    movie_db.release_date = movie_details.release_date
                    movie_db.revenue = movie_details.revenue
                    movie_db.runtime = movie_details.runtime
                    movie_db.status = movie_details.status
                    movie_db.tagline = movie_details.tagline
                    movie_db.title = movie_details.title
                    movie_db.video = movie_details.video
                    movie_db.vote_average = movie_details.vote_average
                    movie_db.vote_count = movie_details.vote_count

                    movie_db.save()

                    # Many to Many relation Movies to Genres

                    for one_of_genres in movie_details.genres:
                        genre, _ = Genres.objects.get_or_create(
                            id=one_of_genres.id,
                            title=one_of_genres.name)
                        movie_db.genres.add(genre)

                    # Many to Many relation Movies to Production Companies

                    for one_of_prodcompany in movie_details.production_companies: # noqa
                        prodcompany, _ = ProductionCompany.objects.get_or_create( # noqa
                            id=one_of_prodcompany.id,
                            name=one_of_prodcompany.name,
                            logo_path=one_of_prodcompany.logo_path,
                            origin_country=one_of_prodcompany.origin_country)
                        movie_db.production_companies.add(prodcompany)

                    # Many to Many relation Movies to Spoken Languages

                    for one_of_sp_language in movie_details.spoken_languages:
                        sp_language, _ = SpokenLanguage.objects.get_or_create(
                            iso_639_1=one_of_sp_language.iso_639_1,
                            name=one_of_sp_language.name)
                        movie_db.spoken_languages.add(sp_language)

                    # Many to Many relation Movies to Casts

                    for one_of_cast in movie_tmdb.credits(
                            movie_id=this_discovered_movie.id).cast:

                        this_person = person_tmdb.details(person_id=one_of_cast.id) # noqa
                        People.objects.get_or_create(
                                birthday=this_person.birthday,
                                known_for_department=this_person.known_for_department, # noqa
                                deathday=this_person.deathday,
                                id=this_person.id,
                                name=this_person.name,
                                also_known_as=this_person.also_known_as,
                                gender=this_person.gender,
                                biography=this_person.biography,
                                popularity=this_person.popularity,
                                place_of_birth=this_person.place_of_birth,
                                profile_path=this_person.profile_path,
                                imdb_id=this_person.imdb_id,
                            )
                        cast, _ = Cast.objects.get_or_create(
                            character=one_of_cast.character,
                            person=People.objects.get(id=one_of_cast.id),
                            order=one_of_cast.order,
                        )

                        movie_db.cast.add(cast)

                    # Many to Many relation Movies to Crews

                    for one_of_crew in movie_tmdb.credits(movie_id=this_discovered_movie.id).crew: # noqa

                        this_person = person_tmdb.details(person_id=one_of_crew.id) # noqa
                        People.objects.get_or_create(
                                birthday=this_person.birthday,
                                known_for_department=this_person.known_for_department, # noqa
                                deathday=this_person.deathday,
                                id=this_person.id,
                                name=this_person.name,
                                also_known_as=this_person.also_known_as,
                                gender=this_person.gender,
                                biography=this_person.biography,
                                popularity=this_person.popularity,
                                place_of_birth=this_person.place_of_birth,
                                profile_path=this_person.profile_path,
                                imdb_id=this_person.imdb_id,
                            )
                        crew, _ = Crew.objects.get_or_create(
                            department=one_of_crew.department,
                            person=People.objects.get(id=one_of_crew.id),
                            job=one_of_crew.job,
                        )
                        movie_db.crew.add(crew)

                page_count += 1
            else:
                break

        self.stdout.write('Finished\n')
