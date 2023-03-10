# Generated by Django 4.1.5 on 2023-01-29 07:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Requester',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=150)),
                ('added_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rider',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=150)),
                ('added_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fromLocation', models.CharField(default='Delhi', max_length=50)),
                ('toLocation', models.CharField(max_length=50)),
                ('rideDateTime', models.DateTimeField()),
                ('isFlexibleTimed', models.BooleanField(default=False)),
                ('travelMedium', models.CharField(choices=[('CAR', 'Car'), ('BUS', 'Bus'), ('TRAIN', 'Train')], max_length=30)),
                ('added_date', models.DateTimeField(auto_now=True)),
                ('rideStatus', models.CharField(choices=[('NOT_STARTED', 'Not Started'), ('IN_TRANSIT', 'In Transit'), ('COMPLETED', 'Completed')], default='NOT_STARTED', max_length=30)),
                ('rider_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.rider')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fromLocation', models.CharField(max_length=100)),
                ('toLocation', models.CharField(max_length=100)),
                ('requiredDateTime', models.DateTimeField()),
                ('isFlexibleTimeAllowed', models.BooleanField(default=False)),
                ('assetCount', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('assetType', models.CharField(choices=[('LAPTOP', 'Laptop'), ('TRAVEL_BAG', 'Travel Bag'), ('PACKAGE', 'Package')], max_length=30)),
                ('assetSensitivity', models.CharField(choices=[('HIGHLY_SENSITIVE', 'Highly Sensitive'), ('SENSITIVE', 'Sensitive'), ('NORMAL', 'Normal')], default='NORMAL', max_length=30)),
                ('deliverTo', models.CharField(max_length=50)),
                ('added_date', models.DateTimeField(auto_now=True)),
                ('requestStatus', models.CharField(choices=[('PENDING', 'Pending'), ('EXPIRED', 'Expired')], default='PENDING', max_length=30)),
                ('deliveryStatus', models.CharField(choices=[('NOT_STARTED', 'Not Started'), ('IN_TRANSIT', 'In Transit'), ('COMPLETED', 'Completed')], default='NOT_STARTED', max_length=30)),
                ('appliedStatus', models.CharField(choices=[('APPLIED', 'Applied'), ('NOT_APPLIED', 'Not Applied')], default='NOT_APPLIED', max_length=30)),
                ('matched_ride', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.ride')),
                ('requester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.requester')),
            ],
        ),
    ]
