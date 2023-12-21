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
from paula_pinto_FINAL_app.views import (
    index, formulario_inscritoView, formulario_institucionView, lista_inscritos, inscrito_detalle, autor)
from rest_framework.routers import DefaultRouter
from paula_pinto_FINAL_app import views


urlpatterns = [
    path('', index.as_view(), name='index'),
    # formularios
    path('formulario_inscrito/', formulario_inscritoView.as_view(),
         name='formulario_inscrito'),
    path('formulario_institucion/', formulario_institucionView.as_view(),
         name='formulario_institucion'),
    # autor
    path('autorJson/', views.autor, name='autor'),
    # funcion class based views
    path('lista_inscritos/', lista_inscritos.as_view(), name='lista_inscritos'),
    path('inscrito_detalle/<int:id>/',
         inscrito_detalle.as_view(), name='inscrito_detalle'),
    # funcion based views
    path('lista_institucion/', views.lista_instituciones, name='lista_institucion'),
    path('institucion_detalle/<int:id>/',
         views.institucion_detalle, name='institucion_detalle')
]
