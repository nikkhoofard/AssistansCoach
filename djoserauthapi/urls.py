from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('account.urls')),
    path('usr/', include('api.urls')),
    path('usr/', include('messageapp.urls'))
]
