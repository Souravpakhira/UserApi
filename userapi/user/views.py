from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .models import User
from .serializers import UserSerializer


class apiOverView(APIView):
    def get(self, request, format=None):
        api_urls = {
            'List all users': 'apis/user-list/',
            'Create new user': 'apis/user-create/',
            'Update user': 'apis/user-update/<str:pk>/',
            'Delete user': 'apis/user-delete/<str:pk>/',
            'Search user': 'apis/user/?search='
        }
        return Response(api_urls)


class userList(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class userCreate(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class userUpdate(APIView):
    def put(self, request, pk, format=None):
        users = User.objects.get(id=pk)
        serializer = UserSerializer(
            instance=users, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class userDelete(APIView):
    def delete(self, request, pk, format=None):
        users = User.objects.get(id=pk)
        users.delete()
        msg = "User deleted sucessfully"
        return Response(msg, status=status.HTTP_204_NO_CONTENT)


class userDetails(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('phone',)
