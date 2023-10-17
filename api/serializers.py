from rest_framework import serializers
from .models import UserAction, Action
from django.contrib.auth import get_user_model
from account.models import User


class UserActionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = UserAction
        fields = "__all__"


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = "__all__"
