from rest_framework import serializers
from api.models import *
from django.utils.timezone import datetime
import pytz
import requests

utc = pytz.UTC

class RiderSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=Rider
        fields="__all__"

class RideSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()    
    class Meta:
        model=Ride
        fields=('id', 'rider_id', 'fromLocation', 'toLocation', 'rideDateTime', 
        'isFlexibleTimed', 'travelMedium', 'added_date')


class RequesterSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=Requester
        fields="__all__"

class RequestSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField() 
    requester_id = serializers.ReadOnlyField()
    requestStatus = serializers.SerializerMethodField()

    def get_requestStatus (self, request):
        requestRequiredTime = request.requiredDateTime.replace(tzinfo = utc)
        currentTime = datetime.now().replace(tzinfo=utc)
        if currentTime > requestRequiredTime:
            return RequestStatus.EXPIRED
        return RequestStatus.PENDING


    # requester_id = RequesterSerializer()

    class Meta:
        model=Request
        fields="__all__"