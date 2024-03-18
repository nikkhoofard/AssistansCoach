import datetime
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .models import Action, UserAction, UserProgram
from .serializers import UserActionSerializer,\
    UserProgramSerializer, CoachSerializer, CoachChooseSerializer,\
    SportmanSerializer, CoachSeeSportmanActionSerializer
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from account.models import Coach, Sportman


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


class CreateUserProgram(CreateAPIView):
    queryset = UserProgram.objects.all()
    serializer_class = UserProgramSerializer

    def create(self, request, *args, **kwargs):
        user_input_data = request.data
        instance = UserProgram(
            user=request.user,
            day=user_input_data['day'],
            action=Action.objects.get(name=user_input_data['action']),
            numbers=user_input_data['numbers'],
            numbers_sets=user_input_data['numbers_sets'],
            time_duration2=(datetime.timedelta(seconds=int(user_input_data['time_duration']))),
        )
        instance.save()
        serializer = UserProgramSerializer(instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ListUserProgram(ListAPIView):
    queryset = UserProgram.objects.all()
    serializer_class = UserProgramSerializer

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(user=user)

class CoachListView(ListAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer


class ChooseCoachView(CreateAPIView):
    serializer_class = CoachChooseSerializer
    # Define a serializer for selecting a teacher

    def create(self, request, *args, **kwargs):
        sportman = Sportman.objects.get(user=request.user)
        # Assuming you have a way to get the current student
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        coach_id = request.data['user_id']
        coach = Coach.objects.get(pk=coach_id)
        sportman.coachs.add(coach)
        return Response({'message': 'Coach selected successfully'},
                        status=status.HTTP_201_CREATED)

#todo : in this class auto fill coach_id with user.id and permision
#only for coach
class SportmanCoachListView(ListAPIView):
    serializer_class = SportmanSerializer

    def get_queryset(self):
        coach_id = self.kwargs['coach_id']
        coach = Coach.objects.get(pk=coach_id)
        return coach.sportmans.all()


#todo : add permision and filter for coach and sportman
class CoachSeeSportmanAction(ListAPIView):
    serializer_class = CoachSeeSportmanActionSerializer

    def get_queryset(self):

        sportman = self.kwargs['sportman_id']
        list_sportman = UserAction.objects.filter(user=sportman)
        return list_sportman
