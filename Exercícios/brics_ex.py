refArquivoEntrada = open("../Tac_2/lib/covid_cases_23_01_2021_clean.csv")

refArquivoEntrada.readline()

for linha in refArquivoEntrada:
    delimite = linha.split(",")
    print(delimite)

refArquivoEntrada.close()