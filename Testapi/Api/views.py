from django.shortcuts import render 

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from Api.serializers import UserSerializer, GroupSerializer

from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import HttpResponse



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
