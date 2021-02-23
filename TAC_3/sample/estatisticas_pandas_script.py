"""
Author: Rebeca Marconi Pereira Raboeira
Date: 19/02/2021
Version: 6
Last update: 23/02/2021
"""

import pandas as pd

# função max coluna qualquer
def Maior(df):
    coluna_ma = str(input("Insira o nome da coluna que deseja saber o valor máximo: "))
    print(coluna_ma)
    Ma = df[coluna_ma].max()
    return Ma

# função min coluna qualquer
def Menor(df):
    coluna_mi = str(input("Insira o nome da coluna que deseja saber o valor mínimo: "))
    print(coluna_mi)
    Mi = df[coluna_mi].min()
    return Mi

# função soma coluna qualquer
def Soma(df):
    coluna_so = str(input("Insira o nome da coluna cujos os valores serão totalizados: "))
    print(coluna_so)
    So = df[coluna_so].sum()
    return So

# função média coluna qualquer
def Media(df):
    coluna_me = str(input("Insira o nome da coluna que deseja calcular a média: "))
    print(coluna_me)
    Me = df[coluna_me].mean()
    return Me

# Uma função que mostra os Top X países com maior número
# de casos em ordem decrescente, onde X é um número inteiro.
def Top_X(df):
    X = int(input("Insira quantos países serão selecionados com o maior número de casos: "))
    print(X)
    casos_totais = df['Total_cases'].max()
    Xx= ([df['Total_cases'] <= casos_totais],df[0:X])
    casos = []
    casos.append(df[0:X])
    return sorted(casos, reverse=True)

# implemente uma função que normalize o número de casos por 100.000 habitantes
# e adicione numa coluna extra do dataframe original chamada “Total_cases_per_100mil”
def Casos_per_100k(df):
    pplt = (df['Total_cases']/df['Population'])
    fatorNormalizacao_Total_cases = (pplt*100000)
    coluna_casos_per_100k = {'#': df['#'],
                             'Country': df['Country'],
                             'Total_cases': df['Total_cases'],
                             'Total_deaths': df['Total_deaths'],
                             'Total_recovered': df['Total_recovered'],
                             'Population':df['Population'],
                             'Total_cases_per_100mil': fatorNormalizacao_Total_cases}
    df_normalizado = pd.DataFrame(coluna_casos_per_100k,
                                  columns=['#', 'Country', 'Total_cases', 'Total_deaths',
                                           'Total_recovered', 'Population','Total_cases_per_100mil'])


    return df_normalizado

