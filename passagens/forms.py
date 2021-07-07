from datetime import datetime
from django import forms
from tempus_dominus.widgets import DatePicker
from passagens.models import Passagem, Pessoa, ClasseViagem
from passagens.validation import *


class PassagemForms(forms.ModelForm):
  data_pesquisa = forms.DateField(label='Data da Pesquisa', disabled=True, initial=datetime.today)
  class Meta:
    model = Passagem
    fields = '__all__'
    labels = {
      'data_ida': 'Data de Ida',
      'data_volta': 'Data de Volta',
      'data_pesquisa': 'Data da Pesquisa',
      'classe_viagem': 'Classe do Vôo',
      'informacoes': 'Informações Extras'
    }
    widgets = {
      'data_ida': DatePicker(),
      'data_volta': DatePicker()
    }

  def clean(self):
    origem = self.cleaned_data.get('origem')
    destino = self.cleaned_data.get('destino')
    data_ida = self.cleaned_data.get('data_ida')
    data_volta = self.cleaned_data.get('data_volta')
    data_pesquisa = self.cleaned_data.get('data_pesquisa')
    lista_de_erros = {}
    campo_tem_algum_numero(origem, 'origem', lista_de_erros)
    campo_tem_algum_numero(destino, 'destino', lista_de_erros)
    origem_destino_iguais(origem, destino, lista_de_erros)
    valida_data_volta(data_ida, data_volta, lista_de_erros)
    valida_data_ida(data_ida, data_pesquisa, lista_de_erros)
    if lista_de_erros is not None:
      for erro in lista_de_erros:
        mensagem = lista_de_erros[erro]
        self.add_error(erro, mensagem)
    return self.cleaned_data

class PessoaForms(forms.ModelForm):
  class Meta:
    model = Pessoa
    exclude = ['nome']