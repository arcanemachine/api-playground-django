from django.contrib.auth import get_user_model
from django.http import HttpResponse
from rest_framework import viewsets, permissions

from . import serializers
from .models import Thing
from .permissions import HasThingPermissions, HasUserPermissions

UserModel = get_user_model()


def api_root(request):
    return HttpResponse("API Root")


class ThingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to view and edit their things
    """
    queryset = Thing.objects.all()
    serializer_class = serializers.ThingSerializer
    permission_classes = [permissions.IsAuthenticated, HasThingPermissions]

    # show all Things if ?all=1
    def filter_queryset(self, queryset):
        if self.request.GET.get('all') == '1' and self.request.user.is_staff:
            queryset = Thing.objects.all()
        else:
            queryset = queryset.filter(user=self.request.user)
        return queryset


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to view and edit their things
    """
    queryset = UserModel.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated, HasUserPermissions]
