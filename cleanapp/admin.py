from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import CityModel, Question, Title,UserProfile, WeekArrangeMorning


class CityInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'City'

class UserAdmin(BaseUserAdmin):
    inlines = (CityInline, )

admin.site.register(CityModel)
admin.site.register(Question)
admin.site.register(Title)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(WeekArrangeMorning)
