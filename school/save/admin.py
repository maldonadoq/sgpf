from django.contrib import admin
from .models import User, UserType, Subject, Student


# Class to see User Type in the admin site.
class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('type', 'photo')


# Class to see User in the admin site.
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'password', 'last_name', 'email', 'phone', 'state')


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_credits')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name')


admin.site.register(Student, StudentAdmin)
admin.site.register(Subject, SubjectAdmin)



admin.site.register(UserType, UserTypeAdmin)    # admin create user-type.
admin.site.register(User, UserAdmin)            # admin create user.