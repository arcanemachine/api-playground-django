from django.http import HttpResponse
from rest_framework import viewsets, permissions
# from rest_framework.decorators import action

from .models import Thing
from .permissions import HasThingPermissions
from .serializers import ThingSerializer


def api_root(request):
    return HttpResponse("API Root")


class ThingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to view and edit their things
    """
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
    permission_classes = [permissions.IsAuthenticated, HasThingPermissions]

    def filter_queryset(self, queryset):
        if self.request.GET.get('all') == '1' and self.request.user.is_staff:
            queryset = Thing.objects.all()
        else:
            queryset = queryset.filter(user=self.request.user)
        return queryset
