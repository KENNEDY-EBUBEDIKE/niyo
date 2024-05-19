from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from apps.users.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'username',
        ]
