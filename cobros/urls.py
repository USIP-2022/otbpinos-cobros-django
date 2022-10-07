from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"Propietario",views.PropietarioViewSet),

urlpatterns = [


    #path('', views.index, name='index'),
    path('', include(router.urls)),
]