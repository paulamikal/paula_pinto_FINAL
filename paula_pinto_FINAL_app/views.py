from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, ListView
from rest_framework import generics, viewsets
from .models import Inscrito, Institucion
from .forms import formulario_institucion, formulario_inscrito
from .serializers import inscrito_serializer, institucion_serializer, autor_serializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
# Create your views here.

class index(TemplateView):
    template_name = 'index.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class formulario_inscritoView(FormView):
    template_name = 'formulario_inscrito.html'

    def get(self, request, *args, **kwargs):
        form = formulario_inscrito()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = formulario_inscrito(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_inscritos')
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
            return redirect('lista_instituciones')  
        return render(request, self.template_name, {'form': form})
    
class lista_inscritos(ListView):
    model = Inscrito
    template_name = 'lista_inscritos.html'

class lista_instituciones(ListView):
    model = Institucion
    template_name = 'lista_instituciones.html'

class inscrito_APIView(generics.ListCreateAPIView):
    queryset = Inscrito.objects.all()
    serializer_class = inscrito_serializer

class institucion_APIView(generics.ListCreateAPIView):
    queryset = Institucion.objects.all()
    serializer_class = institucion_serializer

class autor_APIView(generics.RetrieveAPIView):
    serializer_class = autor_serializer

class autorAPI():
    serializers_class = autor_serializer

@api_view(['GET'])
def autor(request):
    autor_info = {
        'nombre': 'paula mikal pinto',
        'seccion': 'IEI-170-N4',
    }
    serializer = autor_serializer(autor_info)
    return JsonResponse(serializer.data)

 