from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Inscrito, Institucion
from .forms import formulario_inscrito, formulario_institucion
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, FormView
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from .serializers import inscrito_serializer, institucion_serializer, autor_serializer
from rest_framework.response import Response
from .models import Inscrito, Institucion
from .forms import formulario_institucion, formulario_inscrito
from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView

# Create your views here.


class index(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


@api_view(['GET'])
def autor(request):
    autor = {
        'nombre': 'paula mikal pinto',
        'seccion': 'IEI-170-N4'
    }
    return Response(autor)


class formulario_inscritoView(FormView):
    template_name = 'formulario_inscrito.html'

    def get(self, request, *args, **kwargs):
        form = formulario_inscrito()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = formulario_inscrito(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, self.template_name, {'form': form})


class formulario_institucionView(FormView):
    template_name = 'formulario_institucion.html'

    def get(self, request, *args, **kwargs):
        form = formulario_institucion()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = formulario_institucion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, self.template_name, {'form': form})

# inscritos class based views


class lista_inscritos(APIView):
    def get(self, request):
        inscritos = Inscrito.objects.all()
        serializer = inscrito_serializer(inscritos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = inscrito_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class inscrito_detalle(APIView):
    def get_object(self, id):
        try:
            return Inscrito.objects.get(pk=id)
        except Inscrito.DoesNotExist:
            raise Http404

    def get(self, request, id):
        inscrito = self.get_object(id)
        serializer = inscrito_serializer(inscrito)
        return Response(serializer.data)

    def put(self, request, id):
        inscrito = self.get_object(id)
        serializer = inscrito_serializer(inscrito, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        inscrito = self.get_object(id)
        inscrito.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# institucion funcion based views


@api_view(['GET', 'POST'])
def lista_instituciones(request):
    if request.method == 'GET':
        instituciones = Institucion.objects.all()
        serializer = institucion_serializer(instituciones, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = institucion_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE'])
def institucion_detalle(request, id):
    try:
        institucion = Institucion.objects.get(pk=id)
    except Institucion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = institucion_serializer(institucion)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = institucion_serializer(institucion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        institucion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
