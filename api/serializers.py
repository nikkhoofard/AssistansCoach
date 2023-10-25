from rest_framework import serializers
from .models import UserAction, Action
from django.contrib.auth import get_user_model
from account.models import User


class UserActionSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAction
        fields = [
            'action',
            'numbers',
            'numbers_sets',
            'time_duration',
            ]

    def create(self, validated_data):
        user = self.context['request'].user
        return UserAction(user=user, **validated_data)

class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = "__all__"
