from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Aluno
from .forms import AlunoForm

@login_required
def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos/lista_alunos.html', {'alunos': alunos})

@login_required
def detalhe_alunos(request, id):
    aluno = Aluno.objects.get(pk=id)
    return render(request, 'alunos/detalhes.html', {'aluno':aluno})

@login_required
def cadastrar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            # FORMA ANTIGA: form.save
            # COMENTÁRIO: Faltavam os parênteses. Em Python, para executar uma função ou método, 
            # você deve usar (), caso contrário você apenas faz referência ao objeto da função.
            form.save() 

            # FORMA ANTIGA: return redirect('alunos/lista_alunos.html')
            # COMENTÁRIO: O redirect deve apontar para o 'name' definido na sua urls.py ou para uma URL, 
            # não para o caminho do arquivo .html. O Django precisa saber para qual rota enviar o usuário.
            return redirect('lista_alunos') 
            
    else:
        form = AlunoForm()

    # Este return fora do 'if' garante que, se o formulário for inválido, 
    # a página recarregue exibindo os erros de validação específicos do Django.
    return render(request, 'alunos/form_aluno.html', {'form': form})