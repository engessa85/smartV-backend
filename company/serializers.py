from rest_framework import serializers
from .models import Company, Appointment

class CompanySerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)
    user_first_name = serializers.CharField(source = "user.first_name", read_only=True ) 
    class Meta:
        model = Company
        fields = '__all__'
        read_only_fields = ["user", "user_first_name", "created_at", "updated_at"]

    def create(self, validated_data):
        request = self.context["request"]  # Get request context
        validated_data["user"] = request.user  # Assign authenticated user
        return super().create(validated_data)

class AppointmentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)
    user_first_name = serializers.CharField(source = "user.first_name", read_only=True ) 
    company = serializers.SerializerMethodField()
    class Meta:
        model = Appointment
        fields = '__all__'
        read_only_fields = ["user", "user_first_name"]
    
    def get_company(self, obj):
        return {
            "id": obj.company.id,
            "company_name": obj.company.company_name,
            "company_website": obj.company.company_website,
            "company_email": obj.company.company_email,
        }


    def create(self, validated_data):
        request = self.context["request"]  # Get request context
        validated_data["user"] = request.user  # Assign authenticated user
        return super().create(validated_data)

