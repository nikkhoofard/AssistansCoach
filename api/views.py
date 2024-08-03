import datetime
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .models import Action, UserAction, UserProgram, UserProgramName
from .serializers import UserActionSerializer, \
    UserProgramSerializer, CoachSerializer, CoachChooseSerializer, \
    SportmanSerializer, CoachSeeSportmanActionSerializer, \
    UserProgramNameSerializer
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from account.models import Coach, Sportman
from .permissions import IsCoachUser, IsStudentOfTeacher, OwnProgram


class CreateUserAction(CreateAPIView):
    queryset = UserAction.objects.all()
    serializer_class = UserActionSerializer

    def create(self, request, *args, **kwargs):
        user_input_data = request.data
        instance = UserAction(
            user=request.user,
            action=Action.objects.get(name=user_input_data['action']),
            numbers=user_input_data['numbers'],
            weight=user_input_data['weight'],
            score=user_input_data["score"],
            numbers_sets=user_input_data['numbers_sets'],
            time_duration=(datetime.timedelta(seconds=int(user_input_data['time_duration']))),
        )
        instance.save()
        serializer = UserActionSerializer(instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ListUserAction(ListAPIView):
    queryset = UserAction.objects.all()
    serializer_class = UserActionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['time_created', 'action', 'score']

    def get_queryset(self):
       user = self.request.user
       return self.queryset.filter(user=user)


class CreateProgramName(CreateAPIView):
    queryset = UserProgramName.objects.all()
    serializer_class = UserProgramNameSerializer

    def create(self, request, *args, **kwargs):
        input_data = request.data
        instance = UserProgramName(
            user=request.user,
            name_program=input_data["name_program"],
            time_created=datetime.datetime.now())
        instance.save()
        serializer = UserProgramNameSerializer(instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CreateUserProgram(CreateAPIView):
    queryset = UserProgram.objects.all()
    serializer_class = UserProgramSerializer
    permission_classes = [OwnProgram]

    def create(self, request, *args, **kwargs):
        user_input_data = request.data
        user = request.user

        instance = UserProgram(
            user=user,
            user_program_name=UserProgramName.objects.filter(
            user_id=user.id).get(name_program=user_input_data["user_program_name"]),
            day=user_input_data['day'],
            action=Action.objects.get(name=user_input_data['action']),
            numbers=user_input_data['numbers'],
            weight=user_input_data['weight'],
            score=user_input_data["score"],
            numbers_sets=user_input_data['numbers_sets'],
            time_duration2=(datetime.timedelta(
                seconds=int(user_input_data['time_duration']))),
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
    # Define a serializer for selecting a coach

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
        user = self.request.user
        coach = Coach.objects.get(pk=user)
        return coach.sportmans.all()


#todo : add permision and filter for coach and sportman
#نیاز داریم اینجا اطلاعات جزئی ورزشکار نمایش داده بشه با این
# شرط که اون ورزشکار تحت نظر اون مربی باشه

class CoachSeeSportmanAction(ListAPIView):
    serializer_class = CoachSeeSportmanActionSerializer
    permission_classes = [IsCoachUser, IsStudentOfTeacher]

    def get_queryset(self):
        sportman_user_id = self.kwargs.get('sportman_user_id')
        coach_id = self.request.user

        sportman = UserAction.objects.filter(user_id=sportman_user_id)
        return sportman

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        if request.user.is_authenticated and request.user.is_coach:
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({
                "error": "You are not authorized to access this information."},
                            status=403)

