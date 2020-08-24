from rest_framework import serializers
from leads.models import Lead
from django.contrib.auth.models import User

class LeadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lead
        fields = ['id','lead_title', 'lead_text', 'created_at', 'updated_at', 'user']

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email']
