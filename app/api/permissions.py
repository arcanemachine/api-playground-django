from django.contrib.auth import get_user_model
from rest_framework import permissions

from .models import Thing

UserModel = get_user_model()


class HasThingPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if type(obj) != Thing:
            raise TypeError(
                "This permission can only be used with a Thing object.")
        if not request.user.is_authenticated:
            return False
        if request.user.is_staff:
            return True
        return request.user == obj.user


class HasUserPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if type(obj) != UserModel:
            raise TypeError(
                "This permission can only be used with a User object.")
        if not request.user.is_authenticated:
            return False
        if request.user.is_staff:
            return True
        return request.user == obj
