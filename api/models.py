from django.db import models
from django.core.validators import MinValueValidator
from enum import Enum
import uuid

# Create your models here.
# Declaring Riding Models

class AssetTypes (models.TextChoices): 
    LAPTOP = "LAPTOP",
    TRAVEL_BAG = "TRAVEL_BAG",
    PACKAGE = "PACKAGE"

    @classmethod
    def check_key_contained (cls, key):
        return key in cls.__members__

class AssetSensitivity (models.TextChoices):
    HIGHLY_SENSITIVE = "HIGHLY_SENSITIVE",
    SENSITIVE = "SENSITIVE",
    NORMAL = "NORMAL"

class RequestStatus (models.TextChoices):
    PENDING = "PENDING",
    EXPIRED = "EXPIRED"

    @classmethod
    def check_key_contained (cls, key):
        return key in cls.__members__

class Status (models.TextChoices):
    NOT_STARTED = "NOT_STARTED",
    IN_TRANSIT = "IN_TRANSIT",
    COMPLETED = "COMPLETED"

class TravelMedium (models.TextChoices):
    CAR = "CAR",
    BUS = "BUS", 
    TRAIN = "TRAIN"

class AppliedStatus (models.TextChoices):
    APPLIED = "APPLIED",
    NOT_APPLIED = "NOT_APPLIED"

class Requester(models.Model): 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField (max_length=50)
    address = models.CharField (max_length=150)
    added_date = models.DateTimeField (auto_now=True)

class Rider(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField (max_length=50)
    address = models.CharField (max_length=150)
    added_date = models.DateTimeField (auto_now=True)

class Ride(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    rider_id = models.ForeignKey (Rider, on_delete=models.CASCADE)
    fromLocation = models.CharField (max_length=50, default='Delhi')
    toLocation = models.CharField (max_length=50)
    rideDateTime = models.DateTimeField ()
    isFlexibleTimed = models.BooleanField (default=False)
    travelMedium = models.CharField(choices=TravelMedium.choices, max_length=30)

    added_date = models.DateTimeField (auto_now=True)
    rideStatus = models.CharField(choices=Status.choices, default=Status.NOT_STARTED, max_length=30)

class Request(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    requester = models.ForeignKey(Requester, on_delete=models.CASCADE)
    fromLocation = models.CharField(max_length=100)
    toLocation = models.CharField(max_length=100)
    requiredDateTime = models.DateTimeField()
    isFlexibleTimeAllowed = models.BooleanField(default=False)    
    assetCount = models.IntegerField(default=1, validators=[ MinValueValidator(1) ])
    assetType = models.CharField(choices=AssetTypes.choices, max_length=30)
    assetSensitivity = models.CharField(choices=AssetSensitivity.choices, default=AssetSensitivity.NORMAL, max_length=30)
    deliverTo = models.CharField(max_length=50)
    added_date = models.DateTimeField (auto_now=True)

    requestStatus = models.CharField(choices=RequestStatus.choices, default=RequestStatus.PENDING, max_length=30)
    deliveryStatus = models.CharField(choices=Status.choices, default=Status.NOT_STARTED, max_length=30)
    matched_ride = models.ForeignKey(Ride, default=None, null=True, blank=True, on_delete=models.CASCADE)
    appliedStatus = models.CharField(choices=AppliedStatus.choices, default=AppliedStatus.NOT_APPLIED, max_length=30)