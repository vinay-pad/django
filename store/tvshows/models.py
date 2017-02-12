from django.db import models

class Show(models.Model):
    name = models.CharField(max_length=200)
    type_s = models.CharField(max_length=200)
    language = models.CharField(max_length=50)

class Episode(models.Model):
    show = models.ForeignKey(Show, related_name="episodes")
    season = models.SmallIntegerField()
    number = models.SmallIntegerField()
    airdate = models.DateField()
    airstamp = models.DateTimeField()
    runtime = models.SmallIntegerField()
