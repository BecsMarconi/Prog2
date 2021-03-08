"""
Author: Rebeca Marconi Pereira Raboeira
Date: 06/02/2021 - 01:57
Version: 2
Last update:  06/03/2021 - 17:53
"""

# Importações
from Bio import SeqIO

refSequencias = open('C:/Users/rebec/PycharmProjects/Prog2/TAC_4/lib/sequencias.fasta')
N = 1
for i in SeqIO.parse(refSequencias, "fasta"):
    arq_saida = "sequencia_"+str(N)
    arquivo_gerado = SeqIO.write(i, arq_saida, "fasta")
    N = N + 1
print("%d Arquivos foram gerados." %(N-1))

refSequencias.close()

## Os (837) arquivos foram geraos no 'sample' então os movi para o 'Arquivos_Gerados' de forma manual.