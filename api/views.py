from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Organization
from .serializers import OrganizationSerializer
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
from webapp.filters import OrganizationFilter
from rest_framework import permissions


# Create your views here.


# @api_view(['GET'])
# def orgList(request):
#     org = Organization.objects.all()
#     serializer = OrganizationSerializer(org, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def orgView(request, name):
#     org = Organization.objects.get(name=name)
#     serializer = OrganizationSerializer(org, many=True)
#     return Response(serializer.data)

class OrganizationListView(generics.ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = OrganizationFilter
    search_fields = ['name', 'city', 'state', 'country', 'orgHead']
    ordering_fields = '__all__'
    permission_classes = [permissions.IsAuthenticated]

@api_view(['POST'])
def orgCreate(request):
    serializer = OrganizationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response('Not Reachable')

@api_view(['POST'])
def orgUpdate(request, name):
    org = Organization.objects.get(name=name)
    serializer = OrganizationSerializer(instance = org, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def orgDelete(request, name):
    org = Organization.objects.get(name=name)
    org.delete()
    return Response('Item Deleted')