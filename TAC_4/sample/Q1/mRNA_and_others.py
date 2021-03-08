"""
Author: Rebeca Marconi Pereira Raboeira
Date: 05/02/2021 - 00:02
Version: 2
Last update: 06/03/2021 - 01:55
"""

from Bio.Seq import Seq

# Importações
import Exceptions as ex


# Programa Principal
def main():
    sequencia = Seq(ex.exeption())

    mrna = sequencia.transcribe()
    print("\nmRNA: %s\n" % mrna)

    proteina = mrna.translate()
    print("Proteína: %s" % proteina)

    pass
.
if __name__ == '__main__':
    main()
