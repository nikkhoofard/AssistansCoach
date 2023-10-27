import datetime
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .models import Action, UserAction
from .serializers import UserActionSerializer
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response


class CreateUserAction(CreateAPIView):
    queryset = UserAction.objects.all()
    serializer_class = UserActionSerializer

    def create(self, request, *args, **kwargs):
        user_input_data = request.data
        instance = UserAction(
            user=request.user,
            action=Action.objects.get(name=user_input_data['action']),
            numbers=user_input_data['numbers'],
            numbers_sets=user_input_data['numbers_sets'],
            time_duration=(datetime.timedelta(seconds=int(user_input_data['time_duration']))),
        )
        instance.save()
        serializer = UserActionSerializer(instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ListUserAction(ListAPIView):
    queryset = UserAction.objects.all()
    serializer_class = UserActionSerializer

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(user=user)





