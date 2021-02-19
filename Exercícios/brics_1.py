""""
                                            ##   DEU CERTO, BLZ???
import csv

Total_de_Casos = 0

tabela = csv.reader(open("../Tac_2/lib/covid_cases_23_01_2021_clean.csv"), delimiter = ",")

for (num, PAIS, CASOS_TOTAIS, MORTES_TOTAIS, RECUPERADOS, POPULACAO) in tabela:
    print('{} -> {}'.format(PAIS, MORTES_TOTAIS))

"""

brics = ["Brazil", "India", "Russia", "South Africa"]
casos_totais = 0

refArquivoEntrada = open("../Tac_2/lib/covid_cases_23_01_2021_clean.csv")
refArquivoEntrada.readline()

for linha in refArquivoEntrada:
    delimite = linha.split(",")
    if delimite[1] in brics:
        # print("\n" + ",".join(delimite).rstrip())    #printa toda info dos Brics
        taxa_de_recuperados = (int(delimite[4])/int(delimite[2]))
        print('{} -> Taxa de Recuperados: '.format(delimite[1]) + "%f" % taxa_de_recuperados)
        casos_totais = casos_totais + int(delimite[2])

print("\n" + (("Casos Totais = %d") % casos_totais))

refArquivoEntrada.close()