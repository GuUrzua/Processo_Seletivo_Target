# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json

dados_json = open("dados.json", "r")
dados = json.loads(dados_json.read())
dias_no_mes = []

dados_json.close()

def retornar_valor(dados):
    return dados['valor']

#considerando dias com faturamento 0
def sort_crescente_0():
    dados.sort(key=retornar_valor)
    print("O menor valor de faturamento ocorrido em um dia do mês foi: {:.2f}".format(dados[0]['valor']))

#desconsiderando dias com faturamento 0
def sort_crescente():
    dados.sort(key=retornar_valor)
    i = 0
    while dados[i]['valor'] == 0:
        i += 1
    print("O menor valor de faturamento ocorrido em um dia do mês foi: {:.2f}".format(dados[i]['valor']))

def sort_decrescente():
    dados.sort(reverse=True, key=retornar_valor)
    print("O maior valor de faturamento ocorrido em um dia do mês: {:.2f}".format(dados[0]['valor']))

def calculo_media():
    soma = 0
    i = 0
    while i < len(dados):
        if(dados[i]['valor'] != 0):
            dias_no_mes.append(dados[i]['dia'])
            soma += dados[i]['valor']
        i += 1
    media = soma / len(dias_no_mes)
    return media

def dias_superiores_media():
    media = float(calculo_media())
    i = 0
    dias = []
    while i < len(dados):
        if(dados[i]['valor'] > media):
            dias.append(dados[i]['dia'])
        i += 1
    print("Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: ", len(dias))

sort_crescente()
sort_decrescente()
dias_superiores_media()