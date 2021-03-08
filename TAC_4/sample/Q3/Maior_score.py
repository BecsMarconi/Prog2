"""
Author: Rebeca Marconi Pereira Raboeira
Date: 05/02/2021 - 18:03
Version: 7?
Last update: 08/03/2021 - 16:46
"""

"""
Author: Rebeca Marconi Pereira Raboeira
Date: 05/02/2021 - 18:03
Version: 8
Last update: 08/03/2021 - 16:39
"""
from Bio.Blast.Applications import NcbiblastxCommandline

# C:/Users/rebec/PycharmProjects/Prog2/TAC_4/lib/sequenciaDesconhecida.fasta
# C:/Users/rebec/PycharmProjects/Prog2/TAC_4/lib/TriTrypDB-47_TcruziCLBrenerEsmeraldo-like_AnnotatedProteins.fasta

caminho_blast = r"C:\Program Files\NCBI\blast-2.11.0+\bin\blastx.exe"

meuOutPut = "C:/Users/rebec/PycharmProjects/Prog2/TAC_4/lib/out.blastp.outfmt6.txt"

refArquivoFasta = input("Insira o caminho (de forma correta) para o arquivo FASTA: ")
refArquivoMultiFasta = input("Insira o caminho (de forma correta) para o arquivo multi-fasta de proteínas: ")

comando_blast = NcbiblastxCommandline(query=refArquivoFasta,
                                      subject=refArquivoMultiFasta,
                                      outfmt=6,
                                      out=meuOutPut,
                                      evalue=0.05,
                                      cmd=caminho_blast)

print("Executando busca local:")

stdout, stderr = comando_blast()

print("Fim da busca local...")

blast_resultado = open(meuOutPut, "r")

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

    score = hit[bitscore]

    # maior_score = score.max()
    print("Maior Score: {}".format(score))
