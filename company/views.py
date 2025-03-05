from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import CompanySerializer
from .models import Company
from rest_framework.permissions import AllowAny, IsAuthenticated

# Create your views here.

class CompanyListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        companies = Company.objects.all().order_by('-created_at')
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = CompanySerializer(data=request.data,  context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

