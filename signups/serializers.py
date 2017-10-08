
from rest_framework import serializers
from models import SignUp


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUp
        field = ('first_name', 'last_name')
