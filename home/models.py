from django.db import models


class Movie(models.Model):

    backdrop_path = models.TextField(null=True)
    budget = models.IntegerField(null=True)
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
    revenue = models.IntegerField(null=True)
    runtime = models.IntegerField(null=True)
    spoken_languages = models.ManyToManyField('home.SpokenLanguage')
    status = models.ForeignKey('home.Status',
                                on_delete=models.CASCADE)
    tagline = models.TextField(null=True)
    title = models.TextField()
    video = models.BooleanField()
    vote_average = models.IntegerField()
    vote_count = models.IntegerField()
    cast = models.ManyToManyField('home.Cast')
    crew = models.ManyToManyField('home.Crew')


class Person(models.Model):

    birthday = models.DateField(null=True)
    known_for_department = models.TextField(null=True)
    deathday = models.DateField(null=True)
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    also_known_as = models.TextField(null=True)
    gender = models.ForeignKey('home.Gender',
                                on_delete=models.CASCADE)
    biography = models.TextField(null=True)
    popularity = models.IntegerField()
    place_of_birth = models.TextField(null=True)
    profile_path = models.TextField(null=True)
    imdb_id = models.TextField(max_length=9, null=True)


class Genres(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=200)


class Gender(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=200)


class AlternativeTitle(models.Model):

    movie_id = models.ForeignKey('home.Movie', on_delete=models.CASCADE)
    iso_3166_1 = models.TextField()
    title = models.TextField(max_length=200)
    type = models.TextField(max_length=200)


class Status(models.Model):

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

    id = models.AutoField(primary_key=True)
    character = models.TextField()
    person = models.ForeignKey('home.Person',
                                on_delete=models.CASCADE)
    order = models.IntegerField()  # for order to list cast


class Crew(models.Model):

    id = models.AutoField(primary_key=True)
    department = models.IntegerField()
    person = models.ForeignKey('home.Person',
                                on_delete=models.CASCADE)
    job = models.IntegerField()



