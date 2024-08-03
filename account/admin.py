from django.contrib import admin
from account.models import User, DetailSportman
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserModelAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserModelAdmin
    # that reference specific fields on auth.User.
    list_display = ('id', 'email', 'name', 'is_active', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        ('User Credentials', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_admin', 'is_active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserModelAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email', 'id')
    filter_horizontal = ()

class DetailSportmanModelAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserModelAdmin
    # that reference specific fields on auth.User.
    list_display = ["__all__"]
    #list_filter = ('is_admin',)
    #fieldsets = (
       # ('User Credentials', {'fields': ('email', 'password')}),
      #  ('Personal info', {'fields': ('name',)}),
     #   ('Permissions', {'fields': ('is_admin', 'is_active')}),
    #)
    # add_fieldsets is not a standard ModelAdmin attribute. UserModelAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    #add_fieldsets = (
    #    (None, {
    #        'classes': ('wide',),
    #        'fields': ('email', 'name', 'password1', 'password2'),
    #    }),
    #)
    search_fields = ('user__email',)
    ordering = ('user__email', 'id')
    filter_horizontal = ()
# Now register the new UserModelAdmin...
admin.site.register(User, UserModelAdmin)

admin.site.register(DetailSportman)
