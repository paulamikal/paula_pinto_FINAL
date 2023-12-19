from django import forms
from .models import Institucion, Inscrito


class formulario_inscrito(forms.ModelForm):
    class Meta:
        model = Inscrito
        fields = ['id_persona', 'nombre', 'telefono', 'fecha_inscripcion',
                  'institucion', 'hora_inscripcion', 'estado', 'observacion']


class formulario_institucion(forms.ModelForm):
    class Meta:
        model = Institucion
        fields = ['nombre']
