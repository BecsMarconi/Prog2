"""
Author: Rebeca Marconi Pereira Raboeira
Date: 13/02/2021
Version: 3.0
Last update: 17/02/2021
"""

import sys
import estatisticas_script as es

tabela = sys.argv[1]

def main():
    if tabela.endswith(".csv"):
        pais = 1
        casos_totais = 2
        mortes_totais = 3
        recuperados_totais = 4
        populacao = 5
        with open(tabela) as arquivo_csv:
            leitura = tabela.readline()  #(arquivo_csv, delimiter =",")
            casos = 0
            #linha0 = arquivo_csv[]
            for linha in leitura:
                delimitar = linha.split(",")

                maximo = es.Valor_Maximo
                minimo = es.Valor_Minimo
                media = es.Media_1_Coluna

    elif tabela.endswith(".tsv"):
        with open(tabela) as arquivo_tsv:
            pais = 1
            populacao = 2
            mortes_totais = 3
            leitura = tabela.reader(arquivo_tsv, delimiter="\t")

            for linha in leitura:
                maximo = es.Valor_Maximo
                minimo = es.Valor_Minimo
                media = es.Media_1_Coluna