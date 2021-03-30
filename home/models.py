from django.db import models


class Movie(models.Model):

    backdrop_path = models.TextField(null=True)
    budget = models.IntegerField(null=True)
    genres = models.ManyToManyField('home.Genres')
    id = models.AutoField(primary_key=True)
    original_language = models.TextField()
    original_title = models.TextField()
    overview = models.TextField(null=True)
    popularity = models.IntegerField()
    poster_path = models.TextField(null=True)
    production_companies = models.ForeignKey('home.ProductionCompany',
                                             on_delete=models.CASCADE)
    release_date = models.DateField(null=True)
    revenue = models.IntegerField(null=True)
    runtime = models.IntegerField(null=True)
    status = models.ForeignKey('home.Status',
                                on_delete=models.CASCADE)
    tagline = models.TextField(null=True)
    title = models.TextField()
    video = models.BooleanField()
    vote_average = models.IntegerField()
    vote_count = models.IntegerField()
    cast = models.ForeignKey('home.Credits',
                                on_delete=models.CASCADE)


class Person(models.Model):

    also_known_as = models.TextField(null=True)
    biography = models.TextField(null=True)
    birthday = models.DateField(null=True)
    deathday = models.DateField(null=True)
    gender = models.ForeignKey('home.Gender',
                                on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    known_for_department = models.TextField(null=True)
    name = models.TextField()
    place_of_birth = models.TextField(null=True)
    popularity = models.IntegerField()
    profile_path = models.TextField(null=True)


class Genres(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=200)


class Gender(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=200)


class Status(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=200)


class ProductionCompany(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=200)
    logo_path = models.TextField(null=True)
    origin_country = models.TextField(max_length=200)


class Credits(models.Model):

    id = models.AutoField(primary_key=True)
    cast = models.ForeignKey('home.Cast',
                                on_delete=models.SET_NULL, null=True)
    crew = models.ForeignKey('home.Crew',
                                on_delete=models.SET_NULL, null=True)


class Cast(models.Model):

    id = models.AutoField(primary_key=True)
    person = models.ForeignKey('home.Person',
                                on_delete=models.CASCADE)
    character = models.TextField()
    order = models.IntegerField()  # ?


class Crew(models.Model):

    id = models.AutoField(primary_key=True)
    person = models.ForeignKey('home.Person',
                                on_delete=models.CASCADE)
    department = models.IntegerField()
    job = models.IntegerField()




