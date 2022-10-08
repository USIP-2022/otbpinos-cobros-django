# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register
# ADD NEW Routes HERE
    path('cobros/', include('cobros.urls')),  # <-- NEW
    path("", include("apps.home.urls"))             # UI Kits Html files
]

schema_view = get_schema_view(
   openapi.Info(
      title="Sistema de cobros - OTB",
      default_version='v1.0',
      description="Cobro OTB",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="master.yac@gmail.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

if settings.DEBUG:
    urlpatterns += [
       re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
       re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
       re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]