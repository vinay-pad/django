from rest_framework import serializers
from playerdata.models import Player
from salaries.models import Salary

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ('url','playerId', 'nameFirst', 'nameLast',)

class PlayerSalarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Salary
        fields = ('url', 'playerID', 'yearID', 'teamID', 'lgID', 'salary',)

