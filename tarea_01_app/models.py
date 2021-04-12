from django.db import models

'''
class Personaje(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=50, blank = True, null = True)
    #occupation
    img = models.CharField(max_length=50, blank = True, null = True)
    status = models.CharField(max_length=50, blank = True, null = True)
    nickname = models.CharField(max_length=50, blank = True, null = True)
    #appearance
    #better_call_saul_appearance
    portrayed = models.CharField(max_length=50, blank = True, null = True)
    #category

    def __str__(self):
        return self.name


class Capitulo(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    title = models.CharField(max_length=50, blank = True, null = True)
    season = models.IntegerField(blank = True, null = True)
    episode = models.IntegerField(blank = True, null = True)
    air_date = models.CharField(max_length=50, blank = True, null = True)
    #characters
    series = models.CharField(max_length=50, blank = True, null = True)

    def __str__(self):
        return self.title


class Frase(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    quote = models.CharField(max_length=50, blank = True, null = True)
    author = models.CharField(max_length=50, blank = True, null = True)
    series = models.CharField(max_length=50, blank = True, null = True)

    def __str__(self):
        return self.quote
'''