from djoser.serializers import UserCreateSerializer
from account.models import User
from djoser.conf import settings



class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model=User
        fields=('id', 'email', 'name', 'password')