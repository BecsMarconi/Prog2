"""
Author: Rebeca Marconi Pereira Raboeira
Date: 13/02/2021
Version: 9.0
Last update: 18/02/2021
"""

import estatisticas_script2

def main():
    maximo = estatisticas_script2.Valor_Maximo()
    print('Máximo: {}'.format(maximo))

    minimo = estatisticas_script2.Valor_Minimo()
    print('Mínimo: {}'.format(minimo))

    media = estatisticas_script2.Media()
    print('Média: {}'.format( media))

    razao = estatisticas_script2.Razao()
    print('Razão: {}'.format(razao))

    print("Encerrando...")
    pass

if __name__ == "__main__":
    main()