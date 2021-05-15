from django.db import models


class MovieDetails(models.Model):

    backdrop_path = models.TextField(null=True)
    budget = models.BigIntegerField(null=True)
    genres = models.ManyToManyField('home.Genres')
    id = models.AutoField(primary_key=True)
    imdb_id = models.TextField(max_length=9, null=True)
    original_language = models.TextField()
    original_title = models.TextField()
    overview = models.TextField(null=True)
    popularity = models.IntegerField()
    poster_path = models.TextField(null=True)
    production_companies = models.ManyToManyField('home.ProductionCompany')
    release_date = models.DateField(null=True)
    revenue = models.BigIntegerField(null=True)
    runtime = models.IntegerField(null=True)
    spoken_languages = models.ManyToManyField('home.SpokenLanguage')
    status = models.TextField()
    tagline = models.TextField(null=True)
    title = models.TextField()
    video = models.BooleanField()
    vote_average = models.IntegerField()
    vote_count = models.IntegerField()
    cast = models.ManyToManyField('home.Cast')
    crew = models.ManyToManyField('home.Crew')


class People(models.Model):

    birthday = models.DateField(null=True)
    known_for_department = models.TextField(null=True)
    deathday = models.DateField(null=True)
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    also_known_as = models.TextField(null=True)
    gender = models.IntegerField()
    biography = models.TextField(null=True)
    popularity = models.IntegerField()
    place_of_birth = models.TextField(null=True)
    profile_path = models.TextField(null=True)
    imdb_id = models.TextField(max_length=9, null=True)


class Genres(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=200)


class SpokenLanguage(models.Model):

    id = models.AutoField(primary_key=True)
    iso_639_1 = models.TextField(max_length=200)
    name = models.TextField(max_length=200)


class ProductionCompany(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=200)
    logo_path = models.TextField(null=True)
    origin_country = models.TextField(max_length=200)


class Cast(models.Model):

    # id = models.AutoField(primary_key=True)
    character = models.TextField()
    person = models.ForeignKey('home.People',
                               on_delete=models.CASCADE)
    order = models.IntegerField()  # for order to list cast


class Crew(models.Model):

    # id = models.AutoField(primary_key=True)
    department = models.TextField()
    person = models.ForeignKey('home.People',
                               on_delete=models.CASCADE)
    job = models.TextField()
