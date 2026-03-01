from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def home_view(request):
    home = loader.get_template('cursos/home.html')
    return HttpResponse(home.render())

def lista_curso(request):
    curso = curso.objects.all()
    return render(request, 'cursos/lista_curso.html', {'curso': curso})

def detalhe_cursos(request, id):
    curso = curso.objects.get(pk=id)
    return render(request, 'cursos/detalhes.html', {'cursos':curso})