# import os
# import urllib
#
# from django.views import View
# from tmdbv3api import TMDb, Movie, Configuration, Person
#
# from django.shortcuts import render
#
#
# class MainView(View):
#
#     def get(self, request):
#         tmdb = TMDb()
#
#         tmdb.language = 'ru'
#         tmdb.api_key = os.environ.get("TMDB_API_KEY")
#         movie = Movie()
#         people = Person()
#
#         print(movie.credits(movie_id=32334))
#         print("\n\n\n")
#         print(people.details(person_id=2).keys())
#         recommendations = movie.recommendations(movie_id=247, page=1)
#
#         # path_to_image = '{}{}{}'.format(config.info().images.base_url,
#         #                                      config.info().images.poster_sizes[1],
#         #                                      movie.details(movie_id=32334).poster_path)
#         # image = urllib.request.urlretrieve(path_to_image, 'media/image1.png')
#         # print(path_to_image)
#
#     # for recommendation in recommendations:
#     #     print(config.info().images.base_url, config.info().images.backdrop_sizes[2], movie.details(movie_id=32334).backdrop_path)
#     #     break
#     #     return render(request, 'index.html', context={
#     #                     'image': image}
#     #                   )
