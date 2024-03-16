from django.contrib import admin
from .models import UserAction, Action, UserProgram
# Register your models here.

admin.site.register(UserAction)
admin.site.register(Action)
admin.site.register(UserProgram)
