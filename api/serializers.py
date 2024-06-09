from rest_framework import serializers
from .models import UserAction, Action, UserProgram, UserProgramName
from account.models import Coach, Sportman
from django.contrib.auth import get_user_model
from account.models import User
from .models import UserAction
from datetime import datetime


class CoachSeeSportmanActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAction
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'name']


class CoachSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Coach
        fields = ['user_id', 'user']


class CoachChooseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = ["user_id"]


class SportmanSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Sportman
        fields = ['user_id', 'id', 'user']


class UserActionSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAction
        fields = [
            'action',
            'numbers',
            'weight',
            'score',
            'numbers_sets',
            'time_duration',
            ]


class UserProgramNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProgramName
        fields = ["name_program"]




class UserProgramSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProgram
        fields = [
            'action',
            'day',
            'numbers',
            'numbers_sets',
            'weight',
            'score',
            'time_duration2',
            "user_program_name",
            ]


