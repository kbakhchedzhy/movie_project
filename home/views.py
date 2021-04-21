import os
import urllib
from datetime import date, timedelta

from django.views import View
from tmdbv3api import TMDb, Movie, Configuration, Person, Search, Discover

from django.shortcuts import render


class MainView(View):

    def get(self, request):
        tmdb = TMDb()

        tmdb.language = 'ru'
        tmdb.api_key = os.environ.get("TMDB_API_KEY")
