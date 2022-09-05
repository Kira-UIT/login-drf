from dataclasses import field
from django.contrib.auth.models import User
from rest_framework import serializers, validators

class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    field = ('username', 'password', 'email', 'first_name', 'last_name')

    extra_kwargs = {
      'password': {'write_only': True}

    }