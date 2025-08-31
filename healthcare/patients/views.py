from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Patient
from .serializers import PatientSerializer

class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Return only patients created by the logged-in user
        return Patient.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Set the logged-in user as the creator
        serializer.save(user=self.request.user)
