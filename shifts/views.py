from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Client, Shift
from .serializers import ClientSerializer, ShiftSerializer


# Create your views here.
class signupview(APIView):
    def post(self, request):
        data = request.data
        serializer = ClientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success':'account was created succesfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShiftListOrCreate(ListCreateAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
        
        