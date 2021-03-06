# Generated by Django 3.2 on 2021-04-10 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarea_01_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Capitulo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('season', models.IntegerField(blank=True, null=True)),
                ('episode', models.IntegerField(blank=True, null=True)),
                ('air_date', models.CharField(blank=True, max_length=50, null=True)),
                ('series', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Frase',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('quote', models.CharField(blank=True, max_length=50, null=True)),
                ('author', models.CharField(blank=True, max_length=50, null=True)),
                ('series', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='personaje',
            name='char_id',
        ),
        migrations.AlterField(
            model_name='personaje',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
