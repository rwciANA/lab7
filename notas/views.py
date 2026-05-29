from django.shortcuts import render, redirect
from .forms import AlumnoForm, CursoForm, NotaAlumnoCursoForm
from .models import Alumno, Curso, NotaAlumnoCurso


def crear_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_alumnos')
    else:
        form = AlumnoForm()
    return render(request, 'notas/crear_alumno.html', {'form': form})


def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'notas/lista_alumnos.html', {'alumnos': alumnos})


def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cursos')
    else:
        form = CursoForm()
    return render(request, 'notas/crear_curso.html', {'form': form})


def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'notas/lista_cursos.html', {'cursos': cursos})


def crear_nota(request):
    if request.method == 'POST':
        form = NotaAlumnoCursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_notas')
    else:
        form = NotaAlumnoCursoForm()
    return render(request, 'notas/crear_nota.html', {'form': form})


def lista_notas(request):
    notas = NotaAlumnoCurso.objects.select_related('alumno', 'curso').all()
    return render(request, 'notas/lista_notas.html', {'notas': notas})
