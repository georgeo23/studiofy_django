from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken, CoversSerializer
from core.models import Covers
# Create your views here.
@api_view(['GET'])
def current_user(request):
    
    
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):
   
    
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        nameset = User.objects.all()
        serializer = UserSerializerWithToken(nameset, many=True)
        return Response(serializer.data)

   

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CoversSet(APIView):
    def post(self, request):
        serializer = CoversSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request):
        queryset = Covers.objects.all()
        serializer_class = CoversSerializer(queryset, many=True)
        return Response(serializer_class.data)