def ocorrencias(seq="Insira sua sequência: "):
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
            seq1 = str((input(seq)).upper())
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
    print("Sequência válida!")
    ocorrencias = {}
    for n in seq1:
        if n in ocorrencias:
            ocorrencias[n] = ocorrencias[n] + 1
        else:
            ocorrencias[n] = 1
    return ocorrencias