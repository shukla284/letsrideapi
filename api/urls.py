from django.contrib import admin
from django.urls import path,include
from api.views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'requesters', RequesterViewSet)
router.register(r'rides', RideViewSet)
router.register(r'riders', RiderViewSet)
router.register(r'requests', RequestViewSet)
router.register(r'matches', MatchingRequestsViewSet)

urlpatterns = [    
    path('',include(router.urls))     
]