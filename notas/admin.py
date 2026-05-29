from django.contrib import admin
from .models import Alumno, Curso, NotaAlumnoCurso


admin.site.register(Alumno)
admin.site.register(Curso)
admin.site.register(NotaAlumnoCurso)
