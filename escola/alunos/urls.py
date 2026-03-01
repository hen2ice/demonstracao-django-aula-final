from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.lista_alunos, name='lista_alunos'),
    path('detalhes/<int:id>/', views.detalhe_alunos, name='detalhe_alunos'),
    # FORMA ANTIGA: path('novo/', views.cadastrar_aluno)
    # COMENTÁRIO: Adicionei o argumento name='cadastrar_aluno' para manter o padrão 
    # e facilitar chamadas em templates usando {% url 'cadastrar_aluno' %}.
    path('novo/', views.cadastrar_aluno, name='cadastrar_aluno'),
    path('accounts/', include('django.contrib.auth.urls')),
]