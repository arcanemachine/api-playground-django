from django.urls import include, path
from rest_framework import routers

from . import views

app_name = 'api'


# routers
router = routers.DefaultRouter()
router.register(r'things', views.ThingViewSet, basename='thing')


# urls
urlpatterns = [
    path('', include(router.urls)),
]
