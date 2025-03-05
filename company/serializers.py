from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True) 
    class Meta:
        model = Company
        fields = '__all__'
        read_only_fields = ["user", "created_at", "updated_at"]

    def create(self, validated_data):
        request = self.context["request"]  # Get request context
        validated_data["user"] = request.user  # Assign authenticated user
        return super().create(validated_data)