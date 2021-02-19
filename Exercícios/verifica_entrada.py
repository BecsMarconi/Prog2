def lerEntrada(mensagem=" Insira um número: "):
    n = int(input(mensagem))
    print("Valor digitado: ", n)
    return n


def tupla0 (numeros="Digite dois números separdos por espaços: "):
    nu = str(input(numeros))
    li = []
    li.extend(nu)
    print(li)
    print("Valores digitados -> primeiro: {} ; segundo: {} ".format(li[0], li[2]))
    return li[0], li[2]