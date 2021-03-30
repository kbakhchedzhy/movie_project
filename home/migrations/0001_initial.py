# Generated by Django 3.1.7 on 2021-03-30 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('character', models.TextField()),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Credits',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cast', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.cast')),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ProductionCompany',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=200)),
                ('logo_path', models.TextField(null=True)),
                ('origin_country', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('also_known_as', models.TextField(null=True)),
                ('biography', models.TextField(null=True)),
                ('birthday', models.DateField(null=True)),
                ('deathday', models.DateField(null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('known_for_department', models.TextField(null=True)),
                ('name', models.TextField()),
                ('place_of_birth', models.TextField(null=True)),
                ('popularity', models.IntegerField()),
                ('profile_path', models.TextField(null=True)),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.gender')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('backdrop_path', models.TextField(null=True)),
                ('budget', models.IntegerField(null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('original_language', models.TextField()),
                ('original_title', models.TextField()),
                ('overview', models.TextField(null=True)),
                ('popularity', models.IntegerField()),
                ('poster_path', models.TextField(null=True)),
                ('release_date', models.DateField(null=True)),
                ('revenue', models.IntegerField(null=True)),
                ('runtime', models.IntegerField(null=True)),
                ('tagline', models.TextField(null=True)),
                ('title', models.TextField()),
                ('video', models.BooleanField()),
                ('vote_average', models.IntegerField()),
                ('vote_count', models.IntegerField()),
                ('cast', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.credits')),
                ('genres', models.ManyToManyField(to='home.Genres')),
                ('production_companies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.productioncompany')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.status')),
            ],
        ),
        migrations.CreateModel(
            name='Crew',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('department', models.IntegerField()),
                ('job', models.IntegerField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.person')),
            ],
        ),
        migrations.AddField(
            model_name='credits',
            name='crew',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.crew'),
        ),
        migrations.AddField(
            model_name='cast',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.person'),
        ),
    ]
