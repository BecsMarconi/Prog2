"""
(base) C:\Users\rebec>python C:/Users/rebec/PycharmProjects/Prog2/TAC_3/sample/analise_pandas_tabela.py C:/Users/rebec/Downloads/covid_cases_23_01_2021_clean.xlsx
__________________________________________________________________________________________
Colunas (para os cálculos):
Index(['Total_cases', 'Total_deaths', 'Total_recovered', 'Population'], dtype='object')
__________________________________________________________________________________________
Insira o nome da coluna que deseja saber o valor máximo: Total_deaths
Total_deaths
Máximo -> 427588
__________________________________________________________________________________________
__________________________________________________________________________________________
Insira o nome da coluna que deseja saber o valor mínimo: Total_recovered
Total_recovered
Mínimo -> 8
__________________________________________________________________________________________
__________________________________________________________________________________________
Insira o nome da coluna cujos os valores serão totalizados: Total_recovered
Total_recovered
Soma -> 71125831
__________________________________________________________________________________________
__________________________________________________________________________________________
Insira o nome da coluna que deseja calcular a média: Total_deaths
Total_deaths
Média -> 10347.13
__________________________________________________________________________________________
__________________________________________________________________________________________
Insira quantos países serão selecionados com o maior número de casos: 5
5
:Países com maior número de casos:
[    # Country  Total_cases  Total_deaths  Total_recovered  Population
0  15     USA     25561521        427588         15326868   332097997
1  13   India     10655435        153376         10316096  1387641848
2  11  Brazil      8816254        216475          7628438   213411432
3   9  Russia      3698273         68971          3109315   145969890
4   7      UK      3617459         97329          1616307    68087328]
__________________________________________________________________________________________
__________________________________________________________________________________________
:Quantidade de casos por 100.000 habitantes:
    # Country  Total_cases  Total_deaths  Total_recovered  Population  Total_cases_per_100mil
0  15     USA     25561521        427588         15326868   332097997             7696.981382
1  13   India     10655435        153376         10316096  1387641848              767.880777
2  11  Brazil      8816254        216475          7628438   213411432             4131.106716
3   9  Russia      3698273         68971          3109315   145969890             2533.586207
4   7      UK      3617459         97329          1616307    68087328             5312.969544

(198, 7)
__________________________________________________________________________________________

Isso é tudo.
"""