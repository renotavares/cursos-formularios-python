from django.shortcuts import render

from passagens.forms import PassagemForms, PessoaForms


def index(request):
  passagem_form = PassagemForms()
  pessoa_form = PessoaForms()
  contexto = {
    'passagem_form': passagem_form,
    'pessoa_form': pessoa_form
  }
  return render(request, 'index.html', contexto)

def revisao_consulta(request):
  if request.method == 'POST':
    passagem_form = PassagemForms(request.POST)
    pessoa_form = PessoaForms(request.POST)
    contexto = {
      'passagem_form': passagem_form,
      'pessoa_form': pessoa_form
    }
    if passagem_form.is_valid():
      return render(request, 'minha_consulta.html', contexto)
    else:
      return render(request, 'index.html', contexto)