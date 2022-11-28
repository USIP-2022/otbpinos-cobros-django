from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"propietarios",views.PropietarioViewSet),
#router.register(r"Propietario",views.PropietarioViewSet),

urlpatterns = [
    ##path('propietarios/cantidad', views.propietario_contador),
    path('propietarios/create_list', views.PropietarioCreateAndList.as_view(), name='productos'),
    path('', include(router.urls))
]