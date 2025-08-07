from rest_framework import serializers
from . import models # Import your model

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Doctors
        # Option 1: Include all fields
        #fields = '__all__'
        fields = ['doctor_ID', 'first_name', 'last_name', 'specialty',]
        # Option 2: Specify fields to include
        # fields = ['id', 'field1', 'field2', 'related_field']
        # Option 3: Specify fields to exclude
        # exclude = ['internal_field']
        
        # Optional: Make some fields read-only (e.g., id, owner)
        read_only_fields = ['last_name'] 