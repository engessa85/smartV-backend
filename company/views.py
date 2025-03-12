from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import CompanySerializer, AppointmentSerializer
from .models import Company, Appointment
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import get_object_or_404



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
    
    

    

class UserComaniesView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        companies = Company.objects.filter(user=user).order_by("-created_at") 
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, company_id):
        company = get_object_or_404(Company, pk=company_id)
        serializer = CompanySerializer(company, data=request.data, partial=True, context={"request": request})
        print(serializer)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AppointmentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        appointments = Appointment.objects.filter(user = user).order_by("-created_at") 
        serializer = AppointmentSerializer(appointments, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = AppointmentSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, appointment_id):
        appointment = get_object_or_404(Appointment, id=appointment_id, user=request.user)
        serializer = AppointmentSerializer(appointment, data=request.data, partial=True, context={"request": request})
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)