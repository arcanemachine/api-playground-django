from rest_framework import permissions

from .models import Thing


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
