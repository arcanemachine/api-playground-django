from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # project_root
    path('', views.project_root, name='project_root'),

    # apps
    path('api/', include('api.urls')),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/native/',
         include('rest_framework.urls', namespace='rest_framework')),
]
