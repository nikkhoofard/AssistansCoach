from django.urls import path, include
from . import views
from .views import CreateUserAction, ListUserAction
from rest_framework.routers import DefaultRouter


#router = DefaultRouter()
#router.register("create/", CreateAction, basename='action')
#router.register("create-user-action/", CreateUserAction, basename='user-action')
urlpatterns = [
    #path("", include(router.urls)),
    path("action/create/", CreateUserAction.as_view()),
    path("list/", ListUserAction.as_view())

]
