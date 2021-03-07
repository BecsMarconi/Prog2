"""
Author: Rebeca Marconi Pereira Raboeira
Date: 05/02/2021 - 18:03
Version: 7?
Last update: 06/03/2021 - 02:16
"""

from Bio.Blast.Applications import NcbiblastxCommandline

#
# C:/Users/rebec/PycharmProjects/Prog2/TAC_4/lib/sequenciaDesconhecida.fasta
# C:/Users/rebec/PycharmProjects/Prog2/TAC_4/lib/TriTrypDB-47_TcruziCLBrenerEsmeraldo-like_AnnotatedProteins.fasta

caminho_blast = "C:/Users/rebec/miniconda3/envs/Prog2/Lib/site-packages/Bio/Blast/NCBIXML.py"
# por algum motivo a única coisa que se relaciona como blast está nessa pasta e mesmo apagando e reinstalando
# biopython e cia pelo conda, tudo de novo surge nessa mesma pasta

meuOutput = "out.blastp.outfmt6.txt"

refArquivoFasta = open(input("Insira o caminho (de forma correta) para o arquivo FASTA: "))
refArquivoMultiFasta = open(input("Insira o caminho (de forma correta) para o arquivo multi-fasta de proteínas: "))

comando_blast = NcbiblastxCommandline(query=refArquivoFasta,
                                      subject=refArquivoMultiFasta,
                                      outfmt=6,
                                      out=meuOutput,
                                      evalue=0.05,
                                      cmd=caminho_blast)

print("Executando busca local:")

stdout, stderr = comando_blast()

print("Fim da busca local...")

blast_resultado = open(meuOutput, "r")

qseqid = 0
sseqid = 1
pident = 2
length = 3
mismatch = 4
gapopen = 5
qstart = 6
qend = 7
sstart = 8
send = 9
evalue = 10
bitscore = 11

resultado = blast_resultado.read()
s = resultado.split('\n')

for linha in s:
    hit = linha.split('\t')
    print(linha)

    if len(hit) != 12:
        break

    melhor_score = hit[bitscore][-1]
    print("Maior Score: {}".format(melhor_score))

refArquivoMultiFasta.close()
refArquivoFasta.close()