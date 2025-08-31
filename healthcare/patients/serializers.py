from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'user', 'name', 'age', 'gender', 'contact', 'address']
        read_only_fields = ['user']
