from django.shortcuts import render
from salaries.models import Salary
from salaries.serializers import SalarySerializer
from rest_framework import generics
from players.common import StandardResultsSetPagination

class SalaryList(generics.ListCreateAPIView):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer
    pagination_class = StandardResultsSetPagination

class SalaryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer
