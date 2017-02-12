from django.db import models

class Player(models.Model):

    BATS_RIGHT = 'R'
    BATS_LEFT = 'L'
    BATS_CHOICES = (
            (BATS_RIGHT, "Right"),
            (BATS_LEFT, "Left"),
            )
    playerId = models.CharField(max_length=20, primary_key=True)
    birthYear = models.CharField(max_length=4, blank=True)
    birthMonth = models.CharField(max_length=2, blank=True)
    birthDay = models.CharField(max_length=2, blank=True)
    birthCountry = models.CharField(max_length=50, blank=True)
    birthState = models.CharField(max_length=50, blank=True)
    birthCity = models.CharField(max_length=100, blank=True)
    deathYear = models.CharField(max_length=4, blank=True)
    deathMonth = models.CharField(max_length=2, blank=True)
    deathDay = models.CharField(max_length=2, blank=True)
    deathCountry = models.CharField(max_length=50, blank=True)
    deathState = models.CharField(max_length=50, blank=True)
    deathCity = models.CharField(max_length=100, blank=True)
    nameFirst = models.CharField(max_length=100, blank=True)
    nameLast = models.CharField(max_length=100, blank=True)
    nameGiven = models.CharField(max_length=100, blank=True)
    weight = models.CharField(max_length=3, blank=True)
    height = models.CharField(max_length=3, blank=True)
    bats = models.CharField( max_length=1,
                             choices= BATS_CHOICES,
                             default=BATS_RIGHT,
                             blank=True)
    throws = models.CharField(max_length=1,
                              choices = BATS_CHOICES,
                              default = BATS_RIGHT,
                              blank=True)
    debut = models.CharField(max_length=10, blank=True, null=True)
    finalGame = models.CharField(max_length=10, blank=True, null=True)
    retroId = models.CharField(max_length=20,blank=True)
    bbrefId = models.CharField(max_length=20,blank=True)
