from rest_framework import serializers
from salaries.models import Salary

class SalarySerializer(serializers.HyperlinkedModelSerializer):
    playerID = serializers.HyperlinkedRelatedField(view_name='player-detail', read_only=True)
    class Meta:
        model = Salary
        fields = ('url', 'playerID', 'yearID', 'teamID', 'lgID', 'salary', )
