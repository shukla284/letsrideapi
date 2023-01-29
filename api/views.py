from django.shortcuts import render
from rest_framework import viewsets
from .models import Ride, Rider, Request, Requester
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from http import HTTPStatus
from uuid import UUID

class RequestViewSet(viewsets.ModelViewSet):
    
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    def put (self, request, *args, **kwargs):
        queryParams = request.query_params
        matchingRide = queryParams.get('matching_ride')
        
        request_object = Request.objects.get()
        data = request.data

        if request_object.appliedStatus is not data[ 'appliedStatus' ]:
            if request_object is AppliedStatus.NOT_APPLIED:
                request_object.appliedStatus = AppliedStatus.APPLIED
                request_object.matching_ride = matchingRide
            else: 
                return Response({"message": "Already Applied for this request"}, HTTPStatus.BAD_REQUEST)

        data.appliedStatus = AppliedStatus.APPLIED
        request_object.save()
        
        serializer = RequesterSerializer(request_object)
        return Response(serializer.data, HTTPStatus.OK)

    def list(self, request):
        queryParams = request.query_params
        requesterId = queryParams.get('requester_id')
        statusFilterKey = queryParams.get('status')
        assetTypeFilterKey = queryParams.get('assetType')

        if (requesterId != None) :
            queryset = Request.objects.all().filter (requester_id = requesterId).order_by('requiredDateTime')
            if statusFilterKey is not None and RequestStatus.check_key_contained(statusFilterKey): 
                queryset = queryset.filter(status = statusFilterKey)
            if assetTypeFilterKey is not None and AssetTypes.check_key_contained(assetTypeFilterKey):
                queryset = queryset.filter (assetType = assetTypeFilterKey)
        else:
            queryset = Request.objects.all()
            # return Response({"message": "Requester ID not found for request"}, HTTPStatus.BAD_REQUEST)

        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(queryset,  request=request)
        if page is not None:
            requestSerializer = RequestSerializer(page, many = True, context = { 'request': request })        
            return paginator.get_paginated_response(requestSerializer.data)
        else:
            requestSerializer = RequestSerializer(queryset, many = True, context = { 'request': request })    
            return Response (requestSerializer.data, status = HTTPStatus.OK)

class MatchingRequestsViewSet (viewsets.ReadOnlyModelViewSet):
    
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    def list (self, request):
        queryParams = request.query_params
        requesterId = queryParams.get ('requesterId')
        
        if (requesterId != None):
            requesterId = UUID(requesterId).hex
            sqlQuery = 'select * from api_ride join api_request on (api_ride.fromLocation = api_request.fromLocation and api_ride.toLocation = api_request.toLocation and CAST(api_request.requiredDateTime AS DATE) = CAST(api_ride.rideDateTime as DATE)) where api_request.requester_id = \'{requesterId}\''.format(requesterId = requesterId)
            queryset = Ride.objects.raw (sqlQuery)

            # Adding pagination code
            paginator = PageNumberPagination()
            page = paginator.paginate_queryset (queryset, request= request)
            if page is not None: 
                requestSerializer = RideSerializer (page, many = True, context = { 'request': request })
                return paginator.get_paginated_response(requestSerializer.data)
            else:    
                requestSerializer = RideSerializer (queryset, many = True, context = { 'request': request })
                return Response (requestSerializer.data, HTTPStatus.OK)
        else:
            return Response (status=HTTPStatus.BAD_REQUEST)    

class RequesterViewSet(viewsets.ModelViewSet):
    queryset = Requester.objects.all()
    serializer_class = RequesterSerializer

class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer

class RiderViewSet(viewsets.ModelViewSet):
    queryset = Rider.objects.all()
    serializer_class = RiderSerializer


