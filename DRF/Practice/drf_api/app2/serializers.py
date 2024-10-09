from .models import *
from rest_framework import serializers

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields= '__all__'
        # fields = ['name', 'email', 'phone', 'subject', 'details']
        