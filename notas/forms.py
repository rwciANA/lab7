from django import forms
from .models import Alumno, Curso, NotaAlumnoCurso


class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'dni', 'email', 'fecha_nacimiento']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'codigo', 'creditos', 'descripcion']


class NotaAlumnoCursoForm(forms.ModelForm):
    class Meta:
        model = NotaAlumnoCurso
        fields = ['alumno', 'curso', 'nota']
