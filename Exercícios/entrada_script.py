""""
from verifica_entrada import lerEntrada

num = lerEntrada()

if num % 2 == 0:
    print("O número {} é par.".format(num))
else:
    print("O número {} é ímpar.".format(num))
"""

from verifica_entrada import tupla0

teste = tupla0()

if teste[0]> teste[1]:
    print('{} > {}'.format(teste[0], teste[1]))
elif teste[0]< teste[1]:
    print('{} < {}'.format(teste[0], teste[1]))
else:
    print("São iguais.")