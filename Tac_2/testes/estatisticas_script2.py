"""
Author: Rebeca Marconi Pereira Raboeira
Date: 13/02/2021
Version: 1.0
Last update: 18/02/2021
"""
        ####### TESTE ########

with open("C:/Users/rebec/PycharmProjects/Prog2/Tac_2/lib/covid_cases_23_01_2021_clean.csv") as arquivo_csv:
    import csv
    csv.reader(arquivo_csv, delimiter = ",")

with open("C:/Users/rebec/PycharmProjects/Prog2/Tac_2/lib/covid_cases_23_01_2021_clean.csv") as arquivo_csv:
    arquivo_csv.readline()
    for linha in arquivo_csv:
        delimiter = linha.split(",")
        linha0 = delimiter[0]

# função max
def Valor_Maximo (mensagem_ma = "Digite o número da coluna para calcular o valor máximo: "):
    coluna_ma = int(input(mensagem_ma))
    print("Valor digitado: ", coluna_ma)
    return linha[0][coluna_ma] + "->" + (max(linha[coluna_ma]))

# função minimo
def Valor_Minimo(mensagem_mi = "Digite o número da coluna para calcular o valor mínimo: "):
    coluna_mi = int(input(mensagem_mi))
    print("Valor digitado: ", coluna_mi)
    return linha[0][coluna_mi] + "->" + (min(linha[coluna_mi]))

# função média da coluna
def Media(mensagem_me = "Digite o número da coluna para calcular a média: "):
    coluna_me = int(input(mensagem_me))
    print("Valor digitado: ", coluna_me)
    n = sum(linha[coluna_me])
    d = len(linha[coluna_me])
    return linha[0][coluna_me] + "->" + n/d

# função calcula e retorna a razão entre duas colunas quaisquer
def Razao(colunas_ra = "Digite o número das duas colunas (ex: 3 2) para calcular a média: "):
    colunas = int(input(colunas_ra))
    li = []
    li.extend(colunas)
    #print(li)
    print('Valores digitados -> coluna_1: {}; coluna_2: {}.'.format(li[0], li[2]))
    return '{}/{}'.format(linha[0][li[0]], linha[0][li[2]]) + "->" + (sum(linha[li[0]]))/(sum(linha[li[2]]))
