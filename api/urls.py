from django.urls import path, include
from . import views
from .views import CreateAction, CreateUserAction
from rest_framework.routers import DefaultRouter


#router = DefaultRouter()
#router.register("create/", CreateAction, basename='action')
#router.register("create-user-action/", CreateUserAction, basename='user-action')
urlpatterns = [
    #path("", include(router.urls)),
    path("action/create/", CreateAction.as_view()),
    path("user/", CreateUserAction.as_view())

]
