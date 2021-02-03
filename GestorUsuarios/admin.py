from django.contrib import admin
from .models import Profile, ImagesBio
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

# Register your models here.


class ImagesBioInline(admin.TabularInline):
    model = ImagesBio


class ProfileInline(admin.StackedInline):
    model = Profile
    max_num = 1
    can_delete = False


class UserAdmin(AuthUserAdmin):
    inlines = [ProfileInline, ImagesBioInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
