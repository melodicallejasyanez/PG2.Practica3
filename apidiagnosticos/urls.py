"""
URL configuration for apidiagnosticos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from consultas.views import DiagnosticoViewSet, IntervencionViewSet, ApoyoViewSet, SintomasViewSet

router = routers.DefaultRouter()
router.register(r'diagnosticos', DiagnosticoViewSet)
router.register(r'intervenciones', IntervencionViewSet)
router.register(r'apoyos', ApoyoViewSet)
router.register(r'sintomas', SintomasViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]