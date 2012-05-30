from django.contrib import admin
from django.contrib.auth.admin import User
from models import UserProfile

class UserProfileAdmin (admin.ModelAdmin):
    model = UserProfile

admin.site.register(UserProfile, UserProfileAdmin)
