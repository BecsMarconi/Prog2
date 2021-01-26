bases = {'A' : 0,'C' : 0,'T' : 0,'G' : 0}
posicao = 0
sequencia = input("Digite sua sequencia de DNA: ").upper()
lista = []
extd = []
for e in sequencia:
    if e != 'A' and 'G' and 'C' and 'T':
        print("Sequencia invalida!!")
        break
    else:
        lista.append(e)
        extd.extend(lista)
        num = len(extd)
for [i, k, j] in extd():
    if i == k == j:
        bases[i] = bases[i] + 3
    else:
        posicao = posicao + 2
        print(posicao)
        print(bases[i])
        bases[i] = 0