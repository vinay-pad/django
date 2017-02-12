from django.shortcuts import render
from rest_framework import generics
from playerdata.models import Player
from playerdata.serializers import PlayerSerializer, PlayerSalarySerializer
from players.common import StandardResultsSetPagination
from salaries.models import Salary

class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    pagination_class = StandardResultsSetPagination


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class PlayerSalaryDetail(generics.ListCreateAPIView):
    model = Salary
    serializer_class = PlayerSalarySerializer

    def get_queryset(self):
        playerid = self.kwargs['playerid']
        return Salary.objects.filter(playerID__playerId=playerid)
