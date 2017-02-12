from rest_framework import serializers
from customers.models import Customers, Address, Segment, CustomerSegment
from django.shortcuts import get_object_or_404

class SegmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Segment
        fields = ('url', 'segment',)

class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ('url', 'city', 'state', 'zipCode', 'country', 'region',)

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    customerAddress = serializers.HyperlinkedRelatedField(queryset=Address.objects.all(), view_name="address-detail")
    segments = serializers.HyperlinkedRelatedField(view_name="segment-detail", many=True, read_only=True)
    class Meta:
        model = Customers
        fields = ('url', 'customerId', 'customerName', 'customerAddress', 'segments',)

class CustomerSegmentSerializer(serializers.HyperlinkedModelSerializer):
    #customer = serializers.HyperlinkedRelatedField(queryset=Customers.objects.all(), view_name="customers-detail", lookup_field="customerId")
    segment = serializers.HyperlinkedRelatedField(queryset=Segment.objects.all(), view_name="segment-detail")
    customer = serializers.PrimaryKeyRelatedField(queryset=Customers.objects.all())
    class Meta:
        model = CustomerSegment
        fields = ('url', 'customer', 'segment',)
