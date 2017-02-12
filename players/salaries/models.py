from django.db import models
from playerdata.models import Player
from django.core.validators import MaxValueValidator

class Salary(models.Model):
    yearID = models.PositiveIntegerField(validators=[MaxValueValidator(2050)])
    teamID = models.CharField(max_length=3)
    lgID = models.CharField(max_length=2)
    playerID = models.ForeignKey(Player, to_field="playerId")
    salary = models.CharField(max_length=8)

    class Meta:
        unique_together = ('yearID', 'teamID', 'lgID', 'playerID',)


