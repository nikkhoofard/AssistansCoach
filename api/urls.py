from django.urls import path, include
from . import views
from .views import CreateUserAction,\
    ListUserAction, CreateUserProgram, \
    ListUserProgram, CoachListView, ChooseCoachView, SportmanCoachListView,\
    CoachSeeSportmanAction

urlpatterns = [
    path("useraction/create/", CreateUserAction.as_view()),
    path("useraction/list/", ListUserAction.as_view()),

    path("coach/search/", CoachListView.as_view()),
    path("coach/choose/", ChooseCoachView.as_view()),

    path("coach/sportmans/", SportmanCoachListView.as_view()),
    path("coach/sportmans/details/<int:sportman_id>/", CoachSeeSportmanAction.as_view()),

    path("Program/create/", CreateUserProgram.as_view()),
    path("Program/list/", ListUserProgram.as_view()),

]
