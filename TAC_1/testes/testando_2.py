def homopolimeros(seq="Digite sua sequencia de DNA: "):
    # sequencia recebe a entrada do usuario
    sequencia = input(seq)

    # variáveis para as exeções
    bases = "ACTG"
    bases0 = lambda dna: dna.upper() in bases

    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVXWYZÇ"
    alfabeto0 = lambda dna: dna.upper() in alfabeto

    vazio = " "
    vazio0 = lambda dna: dna.upper() in vazio

    valida = False

    # verifica se a sequencia é válida e, caso não seja, avisa qual o tipo de erro
    for dna in sequencia:
        if bases0(dna):
            valida = True
            print("Sequencia válida!")
            break
        elif alfabeto0(dna):
            valida = False
            print("Sequencia inválida! Contém caracteres diferentes de 'ACTG'.")
            break
        elif vazio0(dna):
            valida = False
            print("Sequência inválida! Não há nada aqui.")
            break
        else:
            valida = False
            print("Sequência inválida! Foi feito o uso de caracteres especiais.")
            break

    # caso a sequencia seja valida vai padronizar o tamanho com upper() e extender em uma lista, separando os eltos
    if valida == True:
        sequencia0 = sequencia.upper()
        l = []
        l.append(sequencia0)
        extd = []
        extd.extend(sequencia0)
        x = 0
        p = 1

        # vai rodar enquanto x(o indice)for diferente do tamanho da sequencia
        while x != (len(extd)):
            A = 1
            C = 1
            T = 1
            G = 1
            homopolimero = {}
            base = 0
            while True:
                for elto, i in enumerate(extd):
                    if elto == 'A':
                        if extd[x] == extd[x + p]:
                            base = 'A'
                            A = A + 1
                            x = x + 1
                            p = p + 1
                            i = indice
                        # break
                        elif A >= 3:
                            homopolimero[base] = [p, i]
                        else:
                            x=0
                            p=1
                            A=1

                    elif elto == 'C':
                        if extd[x] == extd[x + p]:
                            base = 'C'
                            C = C + 1
                            x = x + 1
                            p = p + 1
                            i = indice
                        # break
                        elif C >= 3:
                            homopolimero[base] = [p, i]
                        else:
                            C = 1
                            x = 0
                            p = 1
                    elif elto == 'T':
                        if extd[x] == extd[x + p]:
                            base = 'T'
                            T = T + 1
                            x = x + 1
                            p = p + 1
                            indice = i
                        # break
                        elif T>=3:
                            homopolimero[base] = [p, i]
                        else:
                            T = 1
                            x = 0
                            p = 1
                    elif elto == 'G':
                        if extd[x] == extd[x + p]:
                            base = 'G'
                            G = G + 1
                            x = x + 1
                            p = p + 1
                            indice = i
                        elif G>=3:
                        # break
                            homopolimero[base] = [p, i]

            for H in homopolimero:
                print(("%s, %d, %d") % (H, homopolimero[H][0], homopolimero[H][1]))

