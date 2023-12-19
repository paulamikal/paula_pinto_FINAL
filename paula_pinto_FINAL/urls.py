"""
URL configuration for paula_pinto_FINAL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from paula_pinto_FINAL_app.views import (index, formulario_inscritoView, formulario_institucionView,
                                         lista_inscritos, lista_instituciones, inscrito_serializer, institucion_serializer, inscrito_APIView, institucion_APIView, autor)
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('formulario_inscrito/', formulario_inscritoView.as_view(), name='formulario_inscrito'),
    path('formulario_institucion/', formulario_institucionView.as_view(), name='formulario_institucion'),
    path('lista_inscritos/', lista_inscritos.as_view(), name='lista_inscritos'),
    path('lista_instituciones', lista_instituciones.as_view(), name='lista_instituciones'),
    #path('api/v1/', include(router.urls)),
    path('api/v1/inscritos/', inscrito_APIView.as_view(), name='inscrito_api'),
    path('api/v1/institucion/', institucion_APIView.as_view(), name='institucion_api'),
    path('api/v1/autor/', autor, name='autor'), #se le agrega a la url normal, http://127.0.0.1:8000/api/v1/autor/
]
