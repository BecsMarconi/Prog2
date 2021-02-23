# programa principal

# recebe via linha de comando o nome de um arquivo (do tipo xlsx)
import sys
from sys import argv
import xlrd
import pandas as pd


programaPrincipal = sys.argv[0]
refArquivoEntrada = sys.argv[1]


# with pd.ExcelFile("C:/Users/rebec/Downloads/covid_cases_23_01_2021_clean.xlsx") as xlsx:
with pd.ExcelFile(refArquivoEntrada) as xlsx:
    df = pd.read_excel(xlsx)


# importa o módulo “estatisticas_pandas_script.py” para
import estatisticas_pandas_script as eps

# realizar os cálculos estatísticos e imprimir na tela.
def main():
    print('___' * 30)
    print("Colunas (para os cálculos):")
    print(df.columns[2:])

    ### máximo
    print('___'* 30)
    maximo = eps.Maior(df)
    print("Máximo -> %d" % maximo)
    print('___' * 30)

    ### mínimo
    print('___' * 30)
    minimo = eps.Menor(df)
    print("Mínimo -> %d" % minimo)
    print('___' * 30)

    ### soma
    print('___' * 30)
    soma = eps.Soma(df)
    print("Soma -> %d" % soma)
    print('___' * 30)

    ### mediana
    print('___' * 30)
    mediana = eps.Media(df)
    print("Média -> %.2f" % mediana)
    print('___' * 30)
    
    ### TopX
    print('___' * 30)
    topx = eps.Top_X(df)
    print(":Países com maior número de casos:")
    print(topx)
    print('___' * 30)

    ### Casos totais por 100k
    print('___' * 30)
    cem_k = eps.Casos_per_100k(df)
    print(":Quantidade de casos por 100.000 habitantes:")
    df_final = pd.merge(df, cem_k)
    print(df_final.head())
    print('\n{}'.format(df_final.shape))
    print('___' * 30)

    print("\nIsso é tudo.")
    pass

if __name__ == '__main__':
    main()
