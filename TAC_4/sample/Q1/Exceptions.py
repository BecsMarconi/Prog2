"""
Author: Rebeca Marconi Pereira Raboeira
Date: 05/02/2021 - 00:46
Version: 2
Last update: 06/03/2021 - 21:01
"""

# Código ('TAC_1/sample/Questao_1.py')
# modificado para o tratamento de exceções


def sequencia (seq=str(input("Insira sua sequência de DNA: "))):
    return seq

def exeption (seq=sequencia()):
    mesclado = "BDEFHIJKLMNOPQRSUVXWYZÇ"
    mesclado0 = lambda dna: dna.upper() in mesclado

    vazio = " "
    vazio0 = lambda dna: dna.upper() in vazio

    num = "1234567890"
    num0 = lambda dna: dna in num

    especiais = "ACTG"
    especiais0 = lambda dna: dna.upper() not in especiais

    class ErroCaractere(Exception):
        pass

    class ErroVazio(ErroCaractere):
        pass

    class ErroMesclado(ErroCaractere):
        pass

    class ErroNumero(ErroCaractere):
        pass

    class ErroEspeciais(ErroCaractere):
        pass

    while True:
        try:
            seq1 = seq.upper()
            for dna in seq1:
                if mesclado0(dna):
                    raise ErroMesclado
                elif vazio0(dna):
                    raise ErroVazio
                elif num0(dna):
                    raise ErroNumero
                elif especiais0(dna):
                    raise ErroEspeciais
            break

        except ErroMesclado:
            print("Sequencia inválida! Contém caracteres diferentes dos caractees 'ACTG'.")
        except ErroVazio:
            print("Sequência inválida! Não há nada aqui.")
        except ErroNumero:
            print("Sequência inválida! Não insira números.")
        except ErroEspeciais:
            print("Sequência inválida! Foi feito o uso de caracteres especiais.")
    print("Sequência válida!\n\nSua sequência: {}".format(seq1))

    return (seq1)