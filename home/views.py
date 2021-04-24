import os

from django.views import View
from tmdbv3api import TMDb


class MainView(View):

    def get(self, request):
        tmdb = TMDb()

        tmdb.language = 'ru'
        tmdb.api_key = os.environ.get("TMDB_API_KEY")
