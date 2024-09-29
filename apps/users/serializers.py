from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.db import transaction
from django.contrib.auth import get_user_model
from .models import Individual, Position, Company

User = get_user_model()

class CustomRegisterSerializer(RegisterSerializer):
    role = serializers.CharField(required=True)
    company_name = serializers.CharField(max_length=100, required=True)

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'role': self.validated_data.get('role', ''),
            'company_name': self.validated_data.get('company_name', ''),
        }
    
    # after saving user this method will be called
    # transfer to the model if it is needed somewhere else
    def custom_signup(self, request, user):
        company_name = self.cleaned_data['company_name']
        # Get or create Company
        company, created = Company.objects.get_or_create(name=company_name)

        # Get or Create Position
        position, created = Position.objects.get_or_create(role=self.cleaned_data['role'], company=company)

        # Create Individual
        Individual.objects.create(user=user, position=position)

    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        return user
