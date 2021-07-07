def origem_destino_iguais(origem, destino, lista_de_erros):
  if origem == destino:
    lista_de_erros['destino'] = 'Origem e Destino não podem ser iguais!'

def campo_tem_algum_numero(valor_campo, nome_campo, lista_de_erros):
  if any(char.isdigit() for char in valor_campo):
    lista_de_erros[nome_campo] = 'Não inclua números neste campo!'

def valida_data_volta(data_ida, data_volta, lista_de_erros):
  if data_ida > data_volta:
    lista_de_erros['data_volta'] = "Data de ida não pode ser maior que a data de volta!"

def valida_data_ida(data_ida, data_pesquisa, lista_de_erros):
  if data_ida < data_pesquisa:
    lista_de_erros['data_ida'] = "Essa data já passou!"