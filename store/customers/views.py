from django.shortcuts import render
from customers.models import Customers, Address, Segment, CustomerSegment
from customers.serializers import CustomerSerializer, \
                                  AddressSerializer, SegmentSerializer, CustomerSegmentSerializer
from rest_framework import generics
from store.common import StandardResultsSetPagination

class CustomerList(generics.ListCreateAPIView):
    serializer_class = CustomerSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        """
        override to implement search
        """
        queryset = Customers.objects.all()
        name=self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(customerName=name)
        return queryset

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomerSerializer

class AddressList(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    pagination_class = StandardResultsSetPagination

class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class SegmentList(generics.ListCreateAPIView):
    queryset = Segment.objects.all()
    serializer_class = SegmentSerializer
    pagination_class = StandardResultsSetPagination

class SegmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Segment.objects.all()
    serializer_class = SegmentSerializer

class CustomerSegmentList(generics.ListCreateAPIView):
    serializer_class = CustomerSegmentSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        """
        override to implement search
        """
        queryset = CustomerSegment.objects.all()
        name=self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(customer__customerId=name)
        return queryset

class CustomerSegmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomerSegment.objects.all()
    serializer_class = CustomerSegmentSerializer




    #def get_queryset(self):
    #    cust_id = self.kwargs['pk']
    #    return CustomerSegment.objects.filter(customer__customerId=cust_id)
