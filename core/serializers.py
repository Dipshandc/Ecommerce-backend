from djoser.serializers import UserCreateSerializer
from django.contrib.auth.models import User

class UserCreateSerializer(UserCreateSerializer.Meta):
    class Meta:
        model = User
        fields = ['email','username','password']
